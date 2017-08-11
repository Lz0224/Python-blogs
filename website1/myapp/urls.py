#coding=utf-8

from django.conf.urls import url
from myapp.views import *



urlpatterns = [
    url(r'^first/',first),
    url(r'^python/$',bs),
    url(r'^test/$',test),
    url(r'^template/$',test),
    url(r'^time/', display_meta),
    url(r'^wenzi/',tag),
    url(r'^filter/', fil),
    url(r'^extend/',base, name = 'aaaa'),
    url(r'^nav/', nav, ),
    url(r'^static/',load),

]


urlpatterns += [
    url(r'^models/',db_one),
    url(r'^book/',tmt)
]
