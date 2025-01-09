from django.urls import path, re_path

from .views import (
    startup_detail, startup_list, tag_detail,
    tag_list)

urlpatterns = [
    re_path(r'^startup/$',
        startup_list,
        name='organizer_startup_list'),
    re_path(r'^startup/(?P<slug>[\w\-]+)/$',
        startup_detail,
        name='organizer_startup_detail'),
    re_path(r'^tag/$',
        tag_list,
        name='organizer_tag_list'),
    re_path(r'^tag/(?P<slug>[\w\-]+)/$',
        tag_detail,
        name='organizer_tag_detail'),
]
