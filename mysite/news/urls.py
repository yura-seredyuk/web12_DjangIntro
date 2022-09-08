# from django.conf.urls import url
from django.urls import path, re_path, include
from .views import post_list


urlpatterns = [
    # url(r'^$', post_list, name='post_list')
    re_path(r'^$', post_list, name='post_list'),
]
