# from django.conf.urls import url
from django.urls import path, re_path, include
from .views import post_list, post_details


urlpatterns = [
    # url(r'^$', post_list, name='post_list')
    re_path(r'^$', post_list, name='post_list'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', post_details, name='post_details'),
]
