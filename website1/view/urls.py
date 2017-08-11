#coding=utf-8

from django.conf.urls import url
from view.views import *
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^test/(?P<offset>\d{2,4})/$',test),
    url(r'^foo/$',fir,{'template_name':'foo.html'}),
    url(r'^bar/$',fir,{'template_name':'bar.html'}),
]

urlpatterns += [
    url(r'^about/',TemplateView.as_view(template_name = 'about.html')),
    url(r'^about1/',RedirectView.as_view(url="/view/about2/")),
    url(r'^about2/',MyView.as_view()),
    url(r'^login/',login),
    url(r'^logout/',logout),
    url(r'^index/',index),

]
