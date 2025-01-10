from django.urls import path, re_path

from ..views import (
    TagCreate, TagDelete, TagUpdate, tag_detail,
    tag_list)

urlpatterns = [
    re_path(r'^$',
        tag_list,
        name='organizer_tag_list'),
    re_path(r'^create/$',
        TagCreate.as_view(),
        name='organizer_tag_create'),
    re_path(r'^(?P<slug>[\w\-]+)/$',
        tag_detail,
        name='organizer_tag_detail'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$',
        TagDelete.as_view(),
        name='organizer_tag_delete'),
    re_path(r'^(?P<slug>[\w\-]+)/update/$',
        TagUpdate.as_view(),
        name='organizer_tag_update'),
]
