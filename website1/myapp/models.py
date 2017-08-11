# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BookQuerySet(models.QuerySet):
    def litter(self):
        return self.filter(id__lt = 4)

class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model, using = self._db)


    def title_count(self, keyword):
        return self.filter(title__icontains = keyword).count()

class Publisher(models.Model):
    name = models.CharField(max_length = 30,verbose_name = "名字")
    address = models.CharField(max_length = 50,verbose_name ="地址")
    city = models.CharField(max_length = 60,verbose_name = "城市")
    state_province = models.CharField(max_length = 30,verbose_name = "街道")
    country = models.CharField(max_length = 50,verbose_name = "国家")
    website = models.URLField(verbose_name = "网址")
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'publisher'
        ordering = ['name']
        verbose_name = "出版社"
        verbose_name_plural = verbose_name

class Author(models.Model):
    first_name = models.CharField(max_length = 30,verbose_name = "姓")
    last_name = models.CharField(max_length = 40,verbose_name = "名")
    age = models.IntegerField(null = True,default = 12,verbose_name = "年龄")
    email = models.EmailField(blank = True,verbose_name = "电子邮箱")
    def __unicode__(self):
        return "%s %s"%(self.first_name,self.last_name)
    class Meta:
        ordering = ['first_name']
        verbose_name = "作者"
        verbose_name_plural = verbose_name

class Book(models.Model):
    title = models.CharField(max_length = 100 ,verbose_name = "书名")
    publication_date = models.DateField(blank = True,null = True,verbose_name = "出版日期")

    author = models.ManyToManyField(Author,verbose_name = "作者")
    publisher = models.ForeignKey(Publisher,verbose_name = "出版社")
    
    # objects = BookManager()
    objects = models.Manager()
    asd = BookManager()
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['title']
        verbose_name = "图书"
        verbose_name_plural = verbose_name
