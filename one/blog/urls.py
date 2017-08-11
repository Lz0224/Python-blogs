# -*- coding: utf-8 -*-
from django.conf.urls import url

from blog.views import *

from one import settings



urlpatterns = [
    # url(r'^blogmain/[A-Za-z0-9]?$', blogmain, name = 'blogmain'),
    url(r'^blogmain/', blogmain, name = 'blogmain'),
    url(r'^blogadd/$', blogadd, name = 'blogadd'),
    url(r'^blogpeople', blogpeople, name = 'blogpeople'),
    url(r'^oneblog/[A-Za-z0-9]?$', oneblog, name = 'oneblog'),

    url(r'^test$', test),
    url(r'^test1$', test1),

]
