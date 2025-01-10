# from django.conf.urls import url
from django.urls import path, include, re_path

from .views import (
    TagCreate, TagDelete, TagList, TagPageList,
    TagUpdate, tag_detail)

urlpatterns = [
    re_path(r'^$',
        TagList.as_view(),
        name='organizer_tag_list'),
    re_path(r'^create/$',
        TagCreate.as_view(),
        name='organizer_tag_create'),
    re_path(r'^(?P<page_number>\d+)/$',
        TagPageList.as_view(),
        name='organizer_tag_page'),
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