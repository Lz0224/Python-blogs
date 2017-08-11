# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blogs.models import *
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.conf import settings
from django.contrib import auth
from django.db.models import Count
from django.db.models import F,Q
from blogs.forms import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required,permission_required
# import order_by
# Create your views here.

def page(request, ado, n):   #实现分页功能的
    paginator = Paginator(ado, n)
    try:
        p = int(request.GET.get('page', 1))
        ado = paginator.page(p)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        ado = paginator.page(1)
    return ado

def reg(request):
    try:
        errors = []
        if request.method == 'POST':
            reg = User(request.POST)
            if not request.POST.get('num', ''):
                errors.append('请输入正确的账号')
            if not request.POST.get('name', ''):
                errors.append('请填写姓名')
            if not request.POST.get('password', ''):
                errors.append('请填写密码')
            if not request.POST.get('email', ''):
                errors.append('请填写邮箱')
            a = int(request.POST.get('num'))
            # print a
            # print type(a)
            if not a in range(1367112000,1367112300):
                errors.append('对不起，您不可注册')
            # print errors
            if errors == []:
                User.objects.create(num = request.POST.get('num'), username = request.POST.get('name'), password = make_password(request.POST.get('password')), email = request.POST.get('email'))
                return HttpResponseRedirect('/login/')
            else:
                return render(request, 'failure.html', {'errors':errors})
        else:
            reg = User()
    except Exception as e:
        return render(request, 'failure.html', {'errors':"请重新输入"})
    return render(request, 'reg.html',{'num':reg.num, 'name':reg.username, 'password':reg.password, 'email':reg.email})

@permission_required('add_User',login_url = '/login/')
def login(request):
    try:
        errors = []
        if request.method == 'POST':
            username = request.POST.get('name')
            password = request.POST.get('password')
            if not request.POST.get('name', ''):
                errors.append('请填写姓名')
            if not request.POST.get('password', ''):
                errors.append('请填写密码')
            if not errors:
                if not request.user.is_authenticated():
                    user = auth.authenticate(username = username, password = password)
                    if user is not None:
                        auth.login(request, user)
                        return render(request, 'index.html', {})
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
                    else:
                        return render(request, 'failure.html', {'errors':"登入验证失败"})
                        return HttpResponse("账号或者用户名输入错误")
                else:
                    return render(request, 'failure.html', {'errors':"用户已登入"})
                    return HttpResponse("用户已登入")
    except Exception as e:
        return render(request, 'failure.html', {'errors':"登入验证失败"})
    return render(request, 'login.html', {'name':User.username, 'password':User.password, 'errors':errors})

def comment(request):
    article_list1 = Article.objects.all().values('id', 'category', 'title', 'content', 'date_publish', 'click_count')
    article_list = []
    print article_list1, type(article_list1)
    for article in article_list1:
        print type(article),"2222222222222"
        a = article['id']
        k = Article.objects.get(id = a)
        tag = k.tag.all()
        article['tag'] = tag
        comment_count = Comment.objects.filter(art_id = a).count()
        article['comment_count'] = comment_count
        article_list.append(article)
    article_list = article_list.sort()
    return article_list

def global_setting(request):
    SITE_URL = settings.SITE_URL
    SITE_NAME = "lz。。。"
    # SITE_DESC = settings.SITE_DESC
    category_list = Category.objects.all()
    # category = Category.bojects.all()
    click_article_list = Article.objects.all().values('title').order_by('-click_count')[:4]
    # comment_article_list = comment(request)[:3]
    comment_article_list = Article.objects.all().values('title')[:4]
    recommend_article_list = Article.objects.all().filter(is_recommend = 1).order_by('-date_publish')[:5]
    # print recommend_article_list[0].get('id')
    tag_list = Tags.objects.all()
    archive_list = Article.objects.distinct_date()
    ad_list = Ad.objects.all()
    links_list = Links.objects.all()
    comment_form = CommentForm()

    # comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    # article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_count_list]
    return locals()

def archive(request):
    try:
        # 先获取客户端提交的信息
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)
        article_list = page(request, article_list, 3)
    except Exception as e:
        return render(request, 'failure.html', {'errors':'没有归档。。。。'})
    return render(request, 'archive.html', locals())

def article(request):
    try:
        id = request.GET.get('id','')
        comment_count = Comment.objects.filter(art_id = id).count()
        article = Article.objects.all().get(id = id)
        Article.objects.filter(id = id).update(click_count = F('click_count') + 1)
        comment_list = Comment.objects.all().filter(art_id = id)
    except Article.DoesNotExist:
        return render(request, 'failure.html', {'errors':'没有对应的文章'})
    return render(request, 'article.html',{'article':article, 'comment_list':comment_list, 'comment_count':comment_count})

def logout(request):
    auth.logout(request)
    return render(request, 'failure.html', {'errors':"已注销"})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def category(request):
    cid = request.GET.get('cid', '')
    try:
        a = Category.objects.get(id = cid)
        article_list = a.article_set.all()
        article_list = page(request, article_list,3)
    except Exception as e:
        return render(request, 'failure.html', {'errors':"没有此分类文章 %s"%e})
    return render(request, 'category.html', {'article_list':article_list})

def tag(request):
    try:
        name = request.GET.get('tag', '')
        tag = Tags.objects.get(name = name)
        article_list = tag.article_set.all()
        article_list1 = []
        for article in article_list:
            n = article.id
            comment_count = Comment.objects.filter(art_id = n).count()
            article.comment_count = comment_count
            article_list1.append(article)
        article_list = page(request, article_list1, 3)
    except Exception as e:
        return render(request, 'failure.html', {'errors':"没有此标签的文章"})
    return render(request, 'tag.html',{'article_list':article_list, 'name':name})

def comment_post(request):
    comment_form = CommentForm(request.POST)
    print "asd"
    if comment_form.is_valid():
        #获取表单信息
        print "123"
        a = comment_form.cleaned_data
        comment = Comment.objects.create(username=a["author"], email=a["email"], url=a["url"],  content=a["comment"])
    else:
        return render(request, 'failure.html', {'errors': "请重新输入"})
    # try:
    #     comment_form = CommentForm(request.POST)
    #     print "bbb"
    #     if comment_form.is_valid():
    #         #获取表单信息
    #         comment = Comment.objects.create(username=comment_form["author"],
    #                                          email=comment_form["email"],
    #                                          url=comment_form["url"],
    #                                          content=comment_form["comment"],
    #                                          article=comment_form["article"],)
    #         print "aaa"
    #     else:
    #         return render(request, 'failure.html', {'errors': "请重新输入"})
    # except Exception as e:
    #     print "ddd"
    #     return render(request, 'failure.html', {'errors': "请重新评论。"})
    print "CCC"
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def index(request):
    article_list1 = Article.objects.all().values('id', 'category', 'title', 'content', 'date_publish', 'click_count')
    article_list = []
    for article in article_list1:
        print type(article),"2222222222222"
        a = article['id']
        k = Article.objects.get(id = a)
        tag = k.tag.all()
        article['tag'] = tag
        comment_count = Comment.objects.filter(art_id = a).count()
        article['comment_count'] = comment_count
        article_list.append(article)
    article_list = page(request, article_list, 3)
    return render(request, 'index.html', {'article_list':article_list})

def attack(request):
    a = '192.168.0.133:8000'
    return
n = 9
def essay(request):
    try:
        pass
        # if request.method == "POST":
        #     form = ArticleForm(request.POST)
        #     if form.is_valid():
        #         cd = form.cleaned_data
        #         Article.objects.create({'title', 'desc', 'content', 'user', 'tag', 'category'})
        #         return render(request,'success.html',{'reason':'文章添加成功'})
        #     else:
        #         return render(request, 'failure.html',{'errors':'请重新添加文章'})
    except:
        return render(request, 'failure.html',{'errors':'文章添加失败'})
    if request.method == "POST":
        form = ArticleForm(request.POST)
        print "aaaa"
        if form.is_valid():
            global n
            print "ASADDSDF"
            cd = form.cleaned_data
            print "KLKLFJIOJWLKRFHNJQKWH"
            dic = {'id':n, 'title':cd['title'], 'desc':cd['desc'], 'content':cd['content'], 'user':cd['user'], 'category':cd['category']}
            Article.objects.create(**dic)
            print "完成了啊啊啊啊啊啊啊"
            n += 1
            return render(request,'success.html',{'reason':'文章添加成功'})
        else:
            return render(request, 'failure.html',{'errors':'请重新添加文章'})
    form = ArticleForm()
    return render(request, 'essay.html',{'form':form})


def test(request):
    return render(request, 'lala.html',{})
