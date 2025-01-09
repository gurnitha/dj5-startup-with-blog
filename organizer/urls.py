from django.urls import path, re_path

from .views import (
    startup_detail, startup_list, tag_detail,
    tag_list)

urlpatterns = [
    # http://127.0.0.1:7000/startup/
    re_path(r'^startup/$',
        startup_list,
        name='organizer_startup_list'),
    # http://127.0.0.1:7000/startup/medium-startup/
    re_path(r'^startup/(?P<slug>[\w\-]+)/$',
        startup_detail,
        name='organizer_startup_detail'),
    # http://127.0.0.1:7000/tag/
    re_path(r'^tag/$',
        tag_list,
        name='organizer_tag_list'),
    # http://127.0.0.1:7000/tag/django/
    re_path(r'^tag/(?P<slug>[\w\-]+)/$',
        tag_detail,
        name='organizer_tag_detail'),
]
