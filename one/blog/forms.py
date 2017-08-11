# -*- coding: utf-8 -*-
from django import forms

from blog import *

class AddBlog(forms.Form):
    title = forms.CharField(max_length = 100, label = 'title:')
    content = forms.CharField(label = '内容',widget = forms.Textarea)
    image = forms.ImageField()
