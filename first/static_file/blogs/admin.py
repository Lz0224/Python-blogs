# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blogs.models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'click_count',)
    list_display_links = ('title', 'desc',)
    list_editable = ('click_count',)

    fieldsets = (
        (None, {
            'fields':('title', 'date_publish', 'desc', 'content', 'user', 'category', 'tag', 'is_recommend')
        }),
        ('高级设置',{
            'classes':('collapse'),
            'fields':('click_count', 'is_recommend')
        })
    )
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'avater', 'num', 'nickname', 'tel', 'age')
    list_display_links = ('num', 'nickname')
    list_editable = ('avater',)
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_publish')




admin.site.register(User, UserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tags)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Ad, AdAdmin)
