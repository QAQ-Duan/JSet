from django.shortcuts import render, redirect
from django.http import HttpResponse
from contact.SendEmail import SendEmail

# Create your views here.
def send(request):
    if request.method == 'GET':
        return render(request,'contact.html')
    elif request.method == 'POST':
        name = request.POST.get('con_name')
        phone = request.POST.get('con_phone')
        info = request.POST.get('con_subject')
        print(name,phone,info)
        dic = {'name':name, 'phone':phone, 'content':info}
        SendEmail('duanqihan99066@163.com',dic)

        return redirect('/contact')