# from django.conf.urls import url
from django.urls import path, re_path, include
from .views import post_list, post_details, post_edit, post_delete, \
    user_login, user_logout, user_signin


urlpatterns = [
    # url(r'^$', post_list, name='post_list')
    re_path(r'^$', post_list, name='post_list'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', post_details, name='post_details'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'),
    re_path(r'^post/(?P<pk>[0-9]+)/delete/$', post_delete, name='post_delete'),
    re_path(r'^login/$', user_login, name='login'),
    re_path(r'^logout/$', user_logout, name='logout'),
    re_path(r'^register/$', user_signin, name='register'),
]
