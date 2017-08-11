#coding=utf-8
from django import template

register = template.Library()

@register.filter(name = 'asd')

def asd(value):
    if value == 0:
        return '用户未注册'
    if value == 1:
        return '登入失败，请重新登入'
    if value == 2:
        return "注册成功，欢迎来到"
    if value == 3:
        return "注册失败，请重新注册"
    if value == 4:
        return "修改成功"
    if value == 5:
        return "修改失败"
