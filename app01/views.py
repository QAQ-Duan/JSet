from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01 import models
import json
from django.core.paginator import Paginator, EmptyPage
from PIL import Image
import os
import jieba
# Create your views here.

# 主页
def home(request):
    if request.method == 'GET':
        response = {}

        # top 10（公告）的处理，筛选10个也要改
        announcements = models.Announcement.objects.filter()
        # 把这10个公告封装成字典
        a_list = []
        for a in announcements:
            dic = {'a_id': a.id, 'a_title': a.a_title}
            a_list.append(dic)
        # 把列表装进回复字典里
        n = 10 if len(a_list) < 10 else len(a_list)

        response['a_list'] = a_list[::-1][0:n-1]

        # 把uid装进返回字典里
        response['uid'] = request.session['uid']
        uid=request.session['uid']

        # 帖子展示列表，展示自己已发布的活动
        recommends = models.Topic.objects.filter(t_uid=uid).order_by('-id')
        # 推荐列表
        r_list = []

        for t in recommends:
            dic = {'t_id': t.id, 't_title': t.t_title,  't_photo': t.t_photo}
            r_list.append(dic)
        # 把列表装进response
        response['r_list'] = r_list

        # 把uid装进返回字典里
        response['uid'] = request.session['uid']

        # 把所有类别装入返回字典里
        kinds = models.Kind.objects.filter()
        response['kinds'] = kinds

        return render(request, 'home.html', response)

    elif request.method == 'POST':
        print("###")
        p_type = request.POST.get('type')
        response = {'msg': '', 'status': False}
        print(p_type)
        # 删除帖子
        if p_type == 'delete':
            t_id = request.POST.get('t_id')
            models.Topic.objects.filter(id=t_id).delete()
            response['status'] = True
            response['msg'] = '删除成功'
        return HttpResponse(json.dumps(response))

# 所有帖子
def all_tie(request, kid, reply_limit, time_limit):
    uid = request.session.get('uid')
    if request.method == 'GET':
        # 保持搜索条件不丢失
        keys = request.GET.get('keys','')
    if request.method == 'POST':
        # 搜索接收一个字段，接受搜索的关键字
        keys = request.POST.get('keys','')
    topics = models.Topic.objects.filter(t_title__icontains=keys)
    time = models.Topic.objects.filter(t_time__icontains=keys)
    words = set(jieba.lcut(keys))
    new_words = set(jieba.lcut(keys))
    for word in words:
        if len(word) == 1:
            new_words.discard(word)
    for word in new_words:
        tmp1 = models.Topic.objects.filter(t_title__icontains=word)
        tmp2 = models.Topic.objects.filter(t_content__icontains=word)
        tmp3 = models.Topic.objects.filter(t_kind__icontains=word)
        topics = topics|tmp1|tmp2|tmp3
    topics = topics|time
    # 按关键字查询标题里含有关键字的
    # topics = models.Topic.objects.filter(t_title__icontains=keys)
    # tmp = models.Topic.objects.filter(t_content__icontains=keys)
    # topics = topics|tmp
    topics = topics.order_by('-id')
    kinds = models.Kind.objects.filter()
    p = Paginator(topics,8)
    #     # #获取当前的页码数，默认为1
    pages = request.GET.get('page',1)
    result = p.page(pages)
    return render(request, 'all.html', {'topics': result, 'kinds': kinds, 'uid': uid, 'keys': keys})


# 登录注册
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # 验证用户名密码是否正确，然后登陆存入session
        type = request.POST.get('type')
        response = {'msg': '', 'status': False}

        uid = request.POST.get('uid')
        pwd = request.POST.get('pwd')
        if type == 'login':
            if len(models.User.objects.filter(uid=uid, password=pwd)) != 0:
                # 登录成功
                response['status'] = True
                request.session['uid'] = uid
                return HttpResponse(json.dumps(response))
                pass
            else:
                # 登录失败
                response['msg'] = '用户名或者密码错误'
                return HttpResponse(json.dumps(response))
                pass
        elif type == 'register':
            if len(models.User.objects.filter(uid=uid)) != 0:
                response['msg'] = '用户名已存在'
                return HttpResponse(json.dumps(response))
            models.User.objects.create(uid=uid, password=pwd)
            response['status'] = True
            request.session['uid'] = uid
            return HttpResponse(json.dumps(response))


# 发布页
def publish(request):
    if request.method == 'GET':
        kinds = models.Kind.objects.filter()
        response = {
            'kinds': kinds
        }
        return render(request, 'publish.html', response)
    elif request.method == 'POST':
        # session获取uid
        uid = request.session['uid']
        # 提交发布的文章
        t_title = request.POST.get('t_title')
        #t_introduce = request.POST.get('t_introduce')
        contact_kind = request.POST.get('contact_kind')
        t_content = request.POST.get('t_content')
        t_kind = request.POST.get('t_kind')

        location_kind = request.POST.get('location_kind')
        location = request.POST.get('location')
        t_number = request.POST.get('t_number')
        t_time = request.POST.get('t_time')
        t_contact = request.POST.get('t_contact')

        #print(t_title, t_introduce)

        obj = models.Topic.objects.create(t_title=t_title, 
                                          t_content=t_content, t_kind=t_kind, t_uid=uid,
                                          location_kind=location_kind,location=location,t_number=t_number,
                                          t_time=t_time,contact_kind=contact_kind,t_contact=t_contact)
        t_id = obj.id

        # 存帖子图片
        t_photo = request.FILES.get('t_photo', None)
        if t_photo != None:
            t_photo_path = 'static/img/t_photo/' + str(t_id) + '_' + t_photo.name
        else:
            t_photo_path = 'static/img/default.jpg'

        if t_photo:
            # 保存文件
            f = open(os.path.join(t_photo_path), 'wb')
            for line in t_photo.chunks():
                f.write(line)
            f.close()            
            image = Image.open(t_photo_path)
            image = image.resize((641,621))
            image.save(os.path.join(t_photo_path))


        # 把图片路径存入数据库
        models.Topic.objects.filter(id=t_id).update(t_photo='/'+t_photo_path)

        return redirect('/single/' + str(t_id))


# 单个帖子页面
def single(request, tid):
    if request.method == 'GET':
        # 帖子内容
        # 时间类别作者，标题，正文，图片path
        try:
            topic = models.Topic.objects.get(id=tid)
        except Exception as e:
            return redirect('/home')

        t_time = topic.create_time
        t_kind = topic.t_kind
        t_title = topic.t_title
        t_content = topic.t_content
        t_photo = topic.t_photo
        t_uid = topic.t_uid
        location_kind = topic.location_kind
        location = topic.location
        t_number = topic.t_number
        contact_kind = topic.contact_kind
        t_contact = topic.t_contact
        t_time = topic.t_time
        uid = request.session['uid']
        admin_uid = request.session.get('admin_uid')

        response = {
            'tid': tid,
            't_uid': t_uid,
            't_time': t_time,
            't_kind': t_kind,
            't_title': t_title,
            't_content': t_content,
            't_photo': t_photo,
            'location_kind' : location_kind,
            'location' : location,
            't_number' : t_number,
            'contact_kind':contact_kind,
            't_contact' : t_contact,
            't_time' : t_time,
            'uid': uid,
            'admin_uid': admin_uid,
        }

        #同类推荐
        recommends = models.Topic.objects.filter(t_kind=t_kind).order_by('-id')
        recommends_list = []
        for i in recommends:
            if i.id == eval(tid):  
                continue
            else:
                recommends_list.append(i)
        if len(recommends_list) > 4:
            recommends_list = recommends_list[:3]
        response['recommends_list'] = recommends_list
        print(len(recommends_list))

        # 留言内容
        # 留言者，留言时间，留言内容
        replys = models.Reply.objects.filter(r_tid=tid)
        reply_list = []
        for reply in replys:
            single_reply = {
                'r_uid': reply.r_uid,
                'r_time': reply.r_time,
                'r_content': reply.r_content,
                'r_id': reply.id,
            }
            reply_list.append(single_reply)
        response['reply_list'] = reply_list

        return render(request, 'single.html', response)

    elif request.method == 'POST':
        # 判断是否登录
        uid = request.session.get('uid')
        if not uid:
            return redirect('/login')

        # 删除回复，只有评论者本人或者活动发起者才能删除评论
        p_type = request.POST.get('type')
        r_id = request.POST.get('r_id')
        topic = models.Topic.objects.get(id=tid)
        t_uid = topic.t_uid

        if p_type == 'delete':
            response = {'msg': '', 'status': False}
            # 评论者删除本人的评论
            models.Reply.objects.filter(id=r_id,r_uid=uid).delete()
            # 发起活动者（楼主）删除自己发布活动的评论
            if uid==t_uid:
                models.Reply.objects.filter(id=r_id).delete()
            response['status'] = True
            return HttpResponse(json.dumps(response))

        # 进行回复
        r_content = request.POST.get('r_content')

        # 提交数据库
        obj = models.Reply.objects.create(r_tid=tid,r_uid=uid,r_content=r_content)
        return redirect('/single/' + tid)


# 修改密码页面
def edit_pwd(request):
    if request.method == 'GET':
        uid = request.session.get('uid')
        return render(request, 'edit-pwd.html', {'uid': uid})

    if request.method == 'POST':
        uid = request.session.get('uid')
        old = request.POST.get('old_pwd')
        new1 = request.POST.get('new_pwd1')
        new2 = request.POST.get('new_pwd2')
        if new1 == new2 and len(models.User.objects.filter(uid=uid, password=old)) != 0:
            # 核对成功，修改密码
            models.User.objects.filter(uid=uid).update(password=new1)
        return redirect('/home')


# 管理员登录
def admin(request):
    if request.method == 'GET':
        return render(request, 'admin.html')
    elif request.method == 'POST':
        admin_uid = request.POST.get('admin_id')
        admin_pwd = request.POST.get('admin_pwd')

        response = {'msg': '', 'status': False}

        if admin_uid == 'guanliyuan' and admin_pwd == '123456':
            # 管理员登录成功
            response['status'] = True
            request.session['admin_uid'] = 'guanliyuan'
            return HttpResponse(json.dumps(response))
        else:
            response['msg'] = '用户名或者密码错误'
            return HttpResponse(json.dumps(response))


# 公告管理
def announcement(request):
    if not request.session.get('admin_uid'):
        return redirect('/my-admin')

    # 查询所有公告
    if request.method == 'GET':

        announcements = models.Announcement.objects.filter()
        response = {'announcements': announcements}
        return render(request, 'announcement.html', response)

    # 发公告，删公告
    elif request.method == 'POST':
        p_type = request.POST.get('type')
        response = {'msg': '', 'status': False}
        if p_type == 'delete':
            a_id = request.POST.get('a_id')
            models.Announcement.objects.filter(id=a_id).delete()
            response['status'] = True
        elif p_type == 'create':
            # 添加一条公告
            a_title = request.POST.get('a_title')
            a_content = request.POST.get('a_content')
            models.Announcement.objects.create(a_title=a_title, a_content=a_content)
            response['status'] = True
        return HttpResponse(json.dumps(response))


# 帖子管理：标题，简介，时间，
def topic_manage(request):
    if not request.session.get('admin_uid'):
        return redirect('/my-admin')

    if request.method == 'GET':
        topics = models.Topic.objects.filter()
        response = {
            'topics': topics,
        }
        return render(request, 'admin-home.html', response)
    elif request.method == 'POST':
        p_type = request.POST.get('type')
        response = {'msg': '', 'status': False}
        print(p_type)
        # 删除帖子
        if p_type == 'delete':
            t_id = request.POST.get('t_id')
            models.Topic.objects.filter(id=t_id).delete()
            response['status'] = True
        return HttpResponse(json.dumps(response))





# 公告页面
def single_an(request, aid):
    if request.method == 'GET':
        try:
            an = models.Announcement.objects.get(id=aid)
        except Exception as e:
            return '/home'
        a_title = an.a_title
        a_content = an.a_content

        response = {
            'a_title': a_title,
            'a_content': a_content,
        }
        return render(request, 'single-an.html', response)
