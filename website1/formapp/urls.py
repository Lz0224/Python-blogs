from django.conf.urls import url
from formapp.views import *





urlpatterns = [
    url(r'^search_form/',search_form),
    url(r'^search/',search),
    url(r'^thanks/$',thanks),
    # url(r'^time/plus/(\d{1,2})/$',views.hours_ahead),
    url(r'^congtact/$',contact),
]

urlpatterns += [
    url(r'^form/',formtest),
    url(r'^bookform/',bookset)

]
