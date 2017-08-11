from django.conf.urls import *
from blogs.views import *


urlpatterns = [
    url(r'^reg/$', reg, name = 'reg'),
    url(r'^$', index, name = 'index'),
    url(r'^login/$', login, name = 'login'),
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^article/$', article, name = 'article'),
    url(r'^archive/$', archive, name='archive'),
    url(r'^category/$', category, name = 'category'),
    url(r'^tag/$', tag, name = 'tag'),
    url(r'^com/$', comment_post, name = 'comment_post'),
    url(r'^essay/$', essay, name = 'essay')
]

urlpatterns += [
    url(r'^test/',test)

]
