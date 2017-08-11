# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from blog.models import *
from django.template.loader import get_template, render_to_string
from blog.forms import *
from users.models import *
import shutil
import json
import os
import json
import datetime
import uuid
from django.template import Context, Template, RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
# Create your views here.

name = None
user_id = 1

def blogmain(request):
    blog = Blog()
    rank_list = blog.query_five()

    if request.method == 'GET':
        global name
        name = request.COOKIES.get('username')
        allblog = blog.query_by_type('python')
        allblog = page(request, allblog, 6)
        return render(request, 'blogmain.html', {'allblog': allblog,
                    'name': name, 'ranklist': rank_list})
    if request.is_ajax:
        blogType = request.POST.get('type')
        allblog = blog.query_by_type(blogType)
        # print(blogType)
        # print(blogType)

        # print(dir(t.template))
        # content_html = t.render(Context({'allblog': allblog}), request)   #好像在新版本变了...

        content_html = render_to_string('a.html', {'allblog': allblog})
        # print(content_html)

        # payload = {
        #         'content_html': content_html,
        #         'success': True,
        # }

        # Context({'allblog': allblog})
        # render_to_response()

        # t = get_template('blogmain.html')
        # s = t.render(Context({'allblog': allblog}))
        # print('aaa')

        return HttpResponse(content_html, content_type='application/json')

def blogadd(request):
    list_blog = get_thisuserblog()
    if request.method == 'POST':
        blog = Blog()
        title = request.POST.get('title')
        content = request.POST.get('content')

        img = request.FILES.get("img", None)
        mtype = request.POST.get('type')

        imgpath = save_image(img, title)

        date = {'title': title, 'content': content, 'image': imgpath, 'user_id': user_id,
                        'showtime': datetime.datetime.now(), 'blogtype': mtype}
        blog.add_blog(date)
        return render(request, 'peopleblog.html', {'bloglist': list_blog, 'name': name})
    return render(request, 'addblog.html', {'name': name})
    pass

def blogpeople(request):
    user = User()
    global user_id
    user_id = user.query_id(name).id
    list_blog = get_thisuserblog()

    list_blog = page(request, list_blog, 10)
    return render(request, 'peopleblog.html',
            {"bloglist": list_blog, 'name': name,
            'MEDIA_URL': settings.MEDIA_ROOT})
    pass


def save_image(image, title):
    # print(type(image))
    startpath = settings.MEDIA_ROOT + '/' +title
    if os.path.exists(startpath):
        print('')
    else:
        os.mkdir(startpath)
        pass
    endfile = startpath + '/' + str(image)
    with open(endfile, 'wb+') as desc:
        for value in image.chunks():
            desc.write(value)
    return 'http://192.168.0.202:8000/media/' + title + '/' + str(image)



@csrf_exempt
def upload_image(request, dir_name):
    ##################
    #  kindeditor图片上传返回数据格式说明：
    # {"error": 1, "message": "出错信息"}
    # {"error": 0, "url": "图片地址"}
    ##################
    result = {"error": 1, "message": "上传出错"}
    files = request.FILES.get("imgFile", None)
    if files:
        result = image_upload(files, dir_name)
        # result = save_image(files, dir_name)
    return HttpResponse(json.dumps(result), content_type="application/json")

# 图片上传
def image_upload(files, dir_name):
    # 允许上传文件类型
    allow_suffix = ['jpg', 'png', 'jpeg', 'gif', 'bmp']
    file_suffix = files.name.split(".")[-1]
    if file_suffix not in allow_suffix:
        return {"error": 1, "message": "图片格式不正确"}
    relative_path_file = upload_generation_dir(dir_name)
    path = os.path.join(settings.MEDIA_ROOT, relative_path_file)
    if not os.path.exists(path):  # 如果目录不存在创建目录
        os.makedirs(path)
    file_name = str(uuid.uuid1()) + "." + file_suffix
    path_file = os.path.join(path, file_name)
    file_url = settings.MEDIA_URL + relative_path_file + file_name
    open(path_file, 'wb').write(files.file.read())
    return {"error": 0, "url": file_url}

# 目录创建
def upload_generation_dir(dir_name):
    today = datetime.datetime.today()
    dir_name = dir_name + '/%d/%d/' % (today.year, today.month)
    if not os.path.exists(settings.MEDIA_ROOT + dir_name):
        os.makedirs(settings.MEDIA_ROOT + dir_name)
    return dir_name

def oneblog(request):
    if request.method == 'GET':
        title = request.GET.get('title')
        blog = Blog()
        one_blog = blog.query_one(title)
        return render(request, 'oneblog.html', {'oneblog': one_blog})
    pass

def get_thisuserblog():
    blog = Blog()
    list_blog = blog.query_one_all(user_id)
    return list_blog
    pass


def page(request, mlist, pagenumber):
    paginator = Paginator(mlist, pagenumber)
    try:
        p = int(request.GET.get('page', 1))
        mlist = paginator.page(p)
        pass
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        mlist = paginator.page(1)
    return mlist
    pass




@csrf_exempt
def test(request):
    if request.is_ajax:
        print('aaaaaaa')
        a = {}
        a['result'] = 'post_success'
        return HttpResponse(json.dumps(a), content_type='application/json')
    pass

def test1(request):
    if request.method == 'GET':

        return render(request, 'test.html', {})
        pass
    if request.is_ajax:
        print('aaaaaaaaaaaaaaaaaaaaa')
        return HttpResponse('ajax_handle')
        pass
    pass
