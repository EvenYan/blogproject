from django.conf.urls import url

from blog import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]|1[0-2])/$', views.archive, name='archive'),
]