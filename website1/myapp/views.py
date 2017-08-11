# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import F,Q
from django.shortcuts import render,render_to_response
# Create your views here.
import time
from myapp.models import *
from django.http import HttpResponse
from django.template import loader
import datetime


def first(request):
    return HttpResponse("这是什么玩意啊")

def bs(request):
    #方法一：
    t = loader.get_template('lol.html')
    html = t.render({'time':datetime.datetime.now()})
    return HttpResponse(html)

def test(request):
    # 方法二：
    return render_to_response('CSND.html',{})
    t = time.localtime()
    #方法三：
    # return render(request,'time.html',{'datetime':t})
    #利用函数locals()收集局部变量，注意变量的名称已变
    # return render(request,'time.html',locals())


def display_meta(request):
    num = 1
    s = 'hello kitty'
    l = [1, 2, 3, 4, 5, 6]
    t = (1, 2, 3, 4, 5)
    d = {'a':'one', 'b':'two', 'c':'shree'}
    f = fun
    obj = A()

    return render(request, 'cuowu.html',\
    {'num':num, 's':s, 'list':l, 'tuple':t, 'dict':d, 'fun':f(num), "obj":obj})

def global_setting(request):
    NAME = 'Lvze'
    TEL = '15561457709'
    GEYAN = '业精于勤而荒于嬉，行成于思而毁于随'
    return locals()



def fun(a):
    a += 5
    return a

class A(object):
    a = 'class --> a'
    def f(self):
        return "jest a A:fun"

def tag(request):
    error = 'aaaaa'
    l = [1, 2, 3, 4, 5, 6]
    return render(request,'tags.html',{'error':error, 'list':l} )

def fil(request):
    num = 5
    s = 'HELLO KITTY'
    a = 'global_setting.NAME'
    return render(request, 'filter.html', {'num':num, 's':s, 'a':a})

def base(request):
    return render(request,'extend.html',{})

def nav(request):
    s = 2
    return render(request,'nav.html',{'s':s})

def load(request):
    return render(request, 'static.html')

def db_one(request):
    #增加１
    # Author.objects.create(first_name = 'jame', last_name = 'Green', email = '123@qq.com')
    # Book.objects.create(title = "Book8",publication_date = datetime.datetime.now(),publisher_id = 2)
    # Book.objects.create(title = "Book2",publication_date = datetime.datetime.now())
    # Book.objects.create(title = "Book3",publication_date = datetime.datetime.now())
    # Publisher.objects.create(name = "人民",address = "beijing", city = "beijing",state_province = 'haidian',country = 'china')
    # Publisher.objects.create(name = "内蒙",address = "beijing", city = "beijing",state_province = 'haidian',country = 'china')
    # #######增加２
    # obj = Author(first_name = 'Han', last_name = 'meimei', email = '31245@qq.com')
    # obj.save()
    #
    # dic = {'first_name' : 'ewrw', 'last_name' : 'Green', 'email' : '123@qq.com'}
    # obj = Author(**dic)
    # obj.save()
    ########删
    # Author.objects.filter(id__gt = 4).delete()
    #
    ########改１
    # Author.objects.filter(id=17).update(first_name = 'lili')
    #
    #######改２
    # obj = Author.objects.get(id = 14)
    # obj.first_name = 'lucy'
    # obj.save()
    ######查
    # a = Author.objects.all()    #每一条记录生成一个对象
    # b = Author.objects.all().values('email')   #取出所有指定字段的记录
    # c = Author.objects.all().values_list('first_name','email')   #取出所有指定字段的记录
    # d = Author.objects.get(id = 1)   #获取某一记录的对象
    # e = Author.objects.filter(id__gt = 2)
    # #Ｆ，Ｑ函数的操作。。。
    # Book.objects.filter(id__lt = 5).update(publisher_id = 2)

    # Author.objects.filter().update(age = F('age') + 1)  #F函数的应用

    # q = Q()
    # print dir(q)
    # q.connector = 'AND'
    # q.children.append(('first_name','jame'))
    # q.children.append(('age',10))
    #
    # f = Author.objects.filter(q)
    #
    #
    # return HttpResponse(len(f))
    # return HttpResponse('操作完成')
    pass

def tmt(request):
    book1 = Book.objects.get(id = 2)
    s = book1.publisher.name

    pub1 = Publisher.objects.get(id = 1)
    book1_list = pub1.book_set.all()

    author_list = book1.author.all()

    count = Book.asd.get_queryset().litter()
    return HttpResponse(count)
