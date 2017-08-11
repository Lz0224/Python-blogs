# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.models import *
from formapp.forms import *
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.



def search_form(request):
    return render(request,'search_form.html',{})

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        return HttpResponse("I have get the '%s'"%q)
    else:
        return render(request,'search_form.html',{'error':True})

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject')

        if not request.POST.get('email',''):
            errors.append('Enter a email')

        if not request.POST.get('message',''):
            errors.append('Enter a message')

        if not errors:
            return HttpResponseRedirect("/formapp/thanks/")

    return render(request,"congtact_form.html",{'errors':errors,'subject':request.POST.get('subject'),'email':request.POST.get('email'), 'message':request.POST.get('message')})

def thanks(request):
    return HttpResponse("我接受到信息啦～～～～～～～～～～～～～～～～～～～～～～～～～")
    return redirect("接收到信息～～～～～～～～～～～～～～")

def formtest(request):
    if request.method == "POST":  # request.method是在接收前端网页的form
        form = RemarkForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd['subject']
            print cd['mail']
            a = '=' * 30
            print '=' * 30
            return HttpResponseRedirect('/formapp/form/')
    else:
        form = RemarkForm()
    return render(request, 'formset.html',{'form':form})


def bookset(request):
    if request.method == "POST":  # request.method是在接收前端网页的form
        form = BookForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            dic = {'title':cd['title'],'publication_date':cd['publication_date'],'publisher_id':3}
            Book.objects.create(**dic)
            a = '=' * 30
            print '=' * 30
            return HttpResponseRedirect('/formapp/bookform/')
    else:
        form = BookForm()
    return render(request, 'bookset.html',{'form':form})
