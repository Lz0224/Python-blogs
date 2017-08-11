# -*- coding:utf-8 -*-
from django import forms
from blogs.models import *


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('username', 'email', 'url', 'content', 'article', 'user')

class CommentForm(forms.Form):
    author = forms.CharField(widget=forms.TextInput(attrs={"id": "author", "class": "comment_input", "required": "required","size": "25", "tabindex": "1"}), max_length=50,error_messages={"required":"username不能为空",})
    email = forms.EmailField(widget=forms.EmailInput(attrs={"id":"email","type":"email","class": "comment_input", "required":"required","size":"25", "tabindex":"2"}), max_length=50, error_messages={"required":"email不能为空",})
    url = forms.URLField(widget=forms.URLInput(attrs={"id":"url","type":"url","class": "comment_input", "size":"25", "tabindex":"3"}), max_length=100, required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={"id":"comment", "class": "message_input", "required": "required", "cols": "800", "rows": "200", "tabindex": "4"}), error_messages={"required":"评论不能为空",})
    # article = forms.CharField(widget=forms.HiddenInput())

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'desc', 'content', 'user', 'tag', 'category')
        labels = {
            'title':'标题',
            'desc':'描述',
            'content':'内容',
            'user':'用户',
            'tag':'标签',
            'category':'分类',
        }
