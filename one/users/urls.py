# -*- coding: utf-8 -*-
from django.conf.urls import url

from users.views import *

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^main/$', TemplateView.as_view(template_name = 'main.html')),
    url(r'^login/$', login, name = 'login'),
    url(r'^register/$', register, name = 'register'),
]
