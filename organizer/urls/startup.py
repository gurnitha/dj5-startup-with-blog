from django.urls import path, re_path

from ..views import (
    StartupCreate, StartupDelete, StartupUpdate,
    startup_detail, startup_list)

urlpatterns = [
    re_path(r'^$',
        startup_list,
        name='organizer_startup_list'),
    re_path(r'^create/$',
        StartupCreate.as_view(),
        name='organizer_startup_create'),
    re_path(r'^(?P<slug>[\w\-]+)/$',
        startup_detail,
        name='organizer_startup_detail'),
    re_path(r'^(?P<slug>[\w\-]+)/delete/$',
        StartupDelete.as_view(),
        name='organizer_startup_delete'),
    re_path(r'^(?P<slug>[\w\-]+)/update/$',
        StartupUpdate.as_view(),
        name='organizer_startup_update'),
]
