# 交集开发者手册

本项目旨在为交大同学的课外生活提供交流平台，本项目的核心应用是对于需要多人参加的活动同学可以在本平台发布活动寻找伙伴
运行本项目请在项目使用命令行运行
> python manage.py runserver
---

## 环境配置 Requirements

python 3  
django 3.1.7  
sqlite3  
PIL  
jieba  

---

## 功能 Feature

### 用户端 User

- 登录注册 login  
    输入用户名和密码即可注册登录，不允许用户名重名，重名、密码错误将返回提示
- 修改密码 edit-pwd
- 我的主页 home  
    可以查看该用户已发布的活动，并可以选择删除该活动
- 浏览活动 all  
    根据标签、时间、标题内容等因素寻找自己需要的活动
- 发布活动 publish  
    按照提示填入对应表单，点击提交即可发布活动
- 发布评论 single  
    用户点开单个活动页面即可进行评论并删除自己的评论
- 浏览公告 single-an  
    用户可以点击home页的公告查看公告
- 底部链接
    用户可以点击页面底部的外联到达指定网站
- 联系开发者 contact
    用户可以进入联系我们界面给开发者发送邮件

### 管理员 Admin

- 活动管理  
  查看、删除已发布的活动
- 公告管理  
  发布公告、删除、查看公告

---

### 参考项目 Reference

交大柠檬
同去网
<https://github.com/likunhong01/ForumSystem>

***

code by qihan duan 2021/05/08