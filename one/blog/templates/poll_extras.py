from django import template

register = template.Library()

@register.filter(name='cut')
@stringfilter
def cut(value, arg):
    return value.replice(arg, '')
    pass
