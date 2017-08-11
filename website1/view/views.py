# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import F,Q
from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
import time
from myapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
import datetime
from django.views import View



def test(request,offset):
    a = offset
    return HttpResponse(offset)

def fir(request,template_name):
    return render(request,template_name,{})

class MyView(View):
    def get(self,request):
        return HttpResponse('get result')

##########SESSION############
@csrf_exempt
def login(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        if u == 'root' and p == '123':
            request.session['user'] = u
            request.session['is_login'] = True
            request.session.set_expiry(5)
            return HttpResponseRedirect("/view/index/")
    return render(request, 'login.html', {})

@csrf_exempt
def index(request):
    if request.session.get('is_login', None):
        return render(request, 'index.html', {'user':request.session['user']})
    return HttpResponseRedirect("/view/login/")

def  logout(request):
    request.session.clear()
    return HttpResponseRedirect('/view/login/')
