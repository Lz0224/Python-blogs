from django.conf.urls import *
from usr.views import *

urlpatterns = [
    url(r'^reg/',reg, name = 'reg'),
    url(r'^login/',login, name = 'login'),
    url(r'^loginout/',loginout, name = 'loginout'),
    url(r'^thanks/', login_test),
    url(r'^test/',thanks),

]

urlpatterns += [
    url(r'^image/$',postImage),
    url(r'^message/$',message),
]
