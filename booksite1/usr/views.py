#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
#from django.template import RequestContext
from forms import *
from usr.models import *
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.contrib.auth.decorators import login_required,permission_required
from PIL import Image

# Create your views here.

@permission_required('add_User',login_url = '/login/')
def thanks(request):
    return HttpResponse("感谢你的登入")

# @permission_required(login_url = '/thanks/')
def reg(request):       #注册
    try:            #判断是否有post请求
        if request.method == 'POST':
            reg_form = RegForm(request.POST)   #进入注册的页面，在form文件中
            if reg_form.is_valid():   #判断注册是否成功,is_valid表示数据内容是否合法。
                cd = reg_form.cleaned_data
                User.objects.create(username=cd['username'],password=make_password(cd['password']),email=cd['email'],mobile=cd['tel'])

                return HttpResponseRedirect("/login/")  #注册成功后进入登入界面
            else:   #注册失败后，说明失败原因
                return render(request,'failure.html',{'reason':reg_form.errors})
        else:     #注册失败后重新刷新注册页面
            reg_form = RegForm()
    except Exception as e:
        print e
    return render(request,'reg.html',locals())  #注册失败后刷新后的页面，locals收集局部变量


@login_required(login_url = '/login/')
def login_test(request):
    return HttpResponse('欢迎登入')

def login(request):   #登入界面
    errors=[]
    if request.method == 'POST':
        #在('username','')后一个引号中代表的是默认值，也是为了增加安全性能。
        username = request.POST.get('username', '')  #将前端发回的值给username和password
        password = request.POST.get('password', '')
        if not request.POST.get('username',''):# 判断用户名和密码是否为空
            errors.append('Enter a username.')
        if not request.POST.get('password',''):
            errors.append('Enter a password.')
        if not errors:
            #如果没有错误的进入下列if判断，有错误的直接报错和刷新登入界面。
            if not request.user.is_authenticated():# is_authenticated()判断用户是否登入。
                user = auth.authenticate(username=username,password=password)
                if user is not None and user.is_active: #判断用户名是否不存在或者
                    auth.login(request,user)
                    #HTTP_REFERER 来源网址，用于保存上一次登入的网页
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
                else:
                    return HttpResponse('用户名或密码错误.')
            else:
                return HttpResponse("您已经登入")
    return render(request,'user_login.html',{'errors':errors,})

def loginout(request):#退出登入状态，之后进入登入页面
    auth.logout(request)
    return HttpResponseRedirect("/login/")


def postImage(request):
    return render(request, 'image.html',{})

def message(request):
    try:    #图片的上传以及数据库的加载。还有就是request的数据接收，在setting，urls，中配置，建立文件、数据库。
        img = Ad(title = "imgTest", img = request.FILES.get('picfile'))
        img.save()
    except Exception, e:
        return HttpResponse('Errors %s'%e)
    return HttpResponse("post images")

# def message(request):
#     try:
#         imgFile = request.FILES['picfile']
#         img = Image.open(imgFile)
#         img.save('/home/linux/Django/booksite1/media/a.png', 'png')
#     except Exception, e:
#         return HttpResponse('Errors %s'%e)
#     return HttpResponse("post images")
