# -*- coding: utf-8 -*-
from django import forms

from models import *

TOPIC_CHOICES = (
    (1, 'python'),
    (2, 'H5'),
    (3, '3D'),
    (4, 'Java'),
    (5, 'C'),
)

class RegisterClass(forms.Form):
    name = forms.CharField(max_length = 100, label = 'name:')
    age =  forms.IntegerField()
    pwd = forms.CharField(max_length = 100, label = 'password:')
    aginpwd = forms.CharField(max_length = 100, label = 'agin password:')
    occupation = forms.ChoiceField(choices = TOPIC_CHOICES,label = '专业')
    email = forms.EmailField(label = '邮件')
