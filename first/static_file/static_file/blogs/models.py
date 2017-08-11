# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

# Create your models here.
class User(AbstractUser):
    avater = models.ImageField(default = 'static/images/default.png',max_length = 200, blank = True, verbose_name = '头像')
    # password = models.BigIntegerField(verbose_name = "密码")
    num = models.BigIntegerField(default = 1367112000, verbose_name = "账号")
    nickname = models.CharField(max_length = 30, default = "大笨蛋", verbose_name = "昵称")
    # name = models.CharField(max_length = 20, verbose_name = "姓名")
    tel = models.BigIntegerField(null = True, verbose_name = "电话")
    age = models.IntegerField(default = 23, verbose_name = "年龄")
    gender = models.CharField(max_length = 10, default = "男", verbose_name = "性别")
    email = models.EmailField(blank = True, verbose_name = "邮件")
    motto = models.TextField(default = "啦啦啦～", verbose_name = "座右铭")
    def __unicode__(self):
        return self.username
    class Meta:
        db_table = 'userbase'
        ordering = ['num']
        verbose_name = "啦啦啦"
        verbose_name_plural = verbose_name

class Tags(models.Model):
    name = models.CharField(max_length = 20, verbose_name = "标签名称")
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'tags'
        verbose_name = "标签"
        verbose_name_plural = verbose_name

class Category(models.Model):
    name = models.CharField(max_length = 30, verbose_name = "分类名称")
    index = models.IntegerField(default = 100, verbose_name = "分类排序")
    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']
    def __unicode__(self):
        return self.name

class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y/%m Archive')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list

class Article(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "标题")
    desc = models.CharField(max_length = 100, verbose_name = "文章描述")
    content = models.TextField(verbose_name = "文章内容")
    click_count = models.IntegerField(default = 0, verbose_name = "点击次数")
    is_recommend = models.BooleanField(default = False, verbose_name = "是否推荐")
    date_publish = models.DateField(blank = True,default = datetime.datetime.now(), verbose_name = "发布时间")
    user = models.ForeignKey(User, verbose_name = "用户")  #文章与用户多对一。
    tag = models.ManyToManyField(Tags, verbose_name = "标签")  #标签与文章多对多。
    category = models.ForeignKey(Category, verbose_name = "分类")  #文章与分类一对多
    objects = ArticleManager()
    def __unicode__(self):
        return self.title
    class Meta:
        db_table = 'article'
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

class Comment(models.Model):
    content = models.TextField(verbose_name = "评论内容")
    username = models.CharField(max_length = 30, blank = True, null = True, verbose_name = "用户")
    email = models.EmailField(max_length = 50, blank = True, null = True, verbose_name = "邮箱")
    url = models.URLField(max_length = 100, blank = True, null = True, verbose_name = "个人网站")
    date_publish = models.DateTimeField(auto_now_add = True, verbose_name = "发布时间")
    user = models.ForeignKey(User, blank = True, null = True, verbose_name = "用户")  #评论与用户一对多
    art = models.ForeignKey(Article, blank = True, null = True, verbose_name = "文章")  #评论与文章一对多
    pid = models.ForeignKey('self', blank = True, null = True, verbose_name = "父级评论")  #评论与自身的子级评论一对多
    objects = ArticleManager()
    class Meta:
        # db_table = 'comment'
        verbose_name = "评论"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return str(self.id)

class Links(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "标题")
    description = models.CharField(max_length = 200, verbose_name = "友情链接描述")
    callback_url = models.URLField(verbose_name = "url地址")
    date_publish = models.DateTimeField(auto_now_add = True, verbose_name = "发布时间")
    index = models.IntegerField(default = 999, verbose_name = "排列顺序")
    class Meta:
        db_table = 'links'
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']
    def __unciode__(self):
        return self.title

class Ad(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "广告标题")
    description = models.CharField(max_length = 200, verbose_name = "广告描述")
    image = models.ImageField(upload_to = 'ad/%Y/%m', verbose_name = "图片路径")
    callback_url = models.URLField(verbose_name = "回调url")
    date_publish = models.DateTimeField(auto_now_add = True, verbose_name = "发布时间")
    index = models.IntegerField(default = 999, verbose_name = "排列顺序")
    def __unicode__(self):
        return self.title
    class Meta:
        db_table = 'ad'
        verbose_name = "广告"
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']
