# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.conf import settings

from django.db import models, IntegrityError

from models import User

from forms import RegisterClass

from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse

# Create your views here.


def global_settings(request):
    return {
        'LOGIN': '登陆',
        'REGISTER': '注册',
        'OK': '成功:',
        'ERROR': '失败',
        'EMAIL': '邮箱:',
        'NAME': '姓名:',
        'PASSWORD': '密码:',
        'AGIN': '重新输入密码:',
        'ERRORPASSWORD': '密码输入错误...',
        'NOPEOPLE': '查无此人...',
        'GOUSERINFO': '进入个人信息界面',
        'ADDBLOG': '增加一项',
    }
    pass

def login(request):
    if request.method == 'POST':
        user_list = get_all()
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        for value in user_list:
            if value.get('name') == name and value.get('pwd') == pwd:
                # return HttpResponseRedirect('/blog/blogmain/?name=%s' %name)
                respone = HttpResponseRedirect('/blog/blogmain/')
                respone.set_cookie('username',name, 3600)   #清除： response.delete_cookie('username')
                return respone
            elif value.get('name') == name and value.get('pwd') != pwd:
                error = '密码输入错误...'
            elif value.get('name') != name:
                error = '查无此人...'
        return render(request, 'login.html', {'error': error})
    return render(request, 'login.html', {})



# def main(request):
#     return render(request, 'main.html', {})
#     pass



def register(request):
    if request.method == 'POST':
        error = None
        user = User()
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        agin = request.POST.get('agin')
        email = request.POST.get('email')
        occupation = request.POST.get('occupation')
        age = request.POST.get('age')
        print(occupation)
        valus = {'name': name, 'pwd': pwd, 'email': email, 'occupation': occupation, }
        if name == '' or pwd == '' or email == '' or occupation == '' or age == 0:
            error = '选项不能为空'
            return render(request, 'register.html', {'error': error})
        if pwd != agin:
            error = '再次输入密码不同'
            return render(request, 'register.html', {'error': error})
        try:
            user.add_user(valus)
        except IntegrityError:
            error = '该名字已被使用...'
            return render(request, 'register.html', {'error': error})
        return HttpResponseRedirect('/blog/blogmain/?name=%s' %valus.get('name'))
    else:
        return render(request, 'register.html', {})
    pass


def get_all():
    user = User()
    return user.query_all()
    pass
