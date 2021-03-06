from django.conf.urls import url

from blog import views


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    # url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]|1[0-2])/$', views.archive, name='archive'),
    url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]|1[0-2])/$', views.ArchiveView.as_view(), name='archive'),
    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name="tag"),
    # url(r'^search/$', views.search, name='search'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^Search/$', views.new_search, name='new_search'),
    url(r'^poem/$', views.poem, name='poem'),
    url(r'^get_poem', views.get_poem, name='get_poem'),

]