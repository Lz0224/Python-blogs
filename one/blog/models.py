# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from users.models import *


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100, null = False)
    content = models.TextField()
    image = models.CharField(max_length = 200, null = True)
    showtime = models.DateTimeField(null = True)
    pv = models.IntegerField(null = True)
    blogtype = models.CharField(max_length = 200, null = False)
    user = models.ForeignKey(User)
    # objects = models.Manager()

    def __unicode__(self):
        return self.title
        pass

    def query_all(self):
        return Blog.objects.all()
        pass

    def query_one(self, title):
        return Blog.objects.get(title = title)
        pass

    def delete_this(self, title):
        Blog.objects.get(title = title).delete()
        pass

    def change(self, title, content):
        Blog.objects.filter(title).update(title = title, content = content)
        pass

    def add_blog(self, bloginfo):
        self.title = bloginfo.get('title')
        self.showtime = bloginfo.get('showtime')
        self.content = bloginfo.get('content')
        self.image = bloginfo.get('image')
        self.user_id = bloginfo.get('user_id')
        self.blogtype = bloginfo.get('blogtype')
        self.save()
        pass

    def query_one_all(self, user_id):
        return Blog.objects.filter(user_id = user_id)
        pass

    def query_five(self):
        rank_list = []
        all_list = Blog.objects.all().order_by('showtime')
        i = 0
        if len(all_list) < 5:
            return all_list
            pass
        for value in all_list:
            rank_list.append(value)
            i += 1
            if i == 5:
                return rank_list
                pass
            pass
        pass

    def query_by_type(self, mtype):
        return Blog.objects.filter(blogtype = mtype)
        pass

class Comments(models.Model):
    name = models.CharField(max_length = 30, unique=True,  null = False)
    content = models.TextField()
    user = models.ForeignKey(Blog)

    def get_blog_com(self, userId):
        return Blog.objects.filter(user_id = userId)
        pass
