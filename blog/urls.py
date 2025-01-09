from django.urls import path, re_path

from .views import PostList, post_detail

urlpatterns = [
    # http://127.0.0.1:7000/blog/
    re_path(r'^$',
        PostList.as_view(),
        name='blog_post_list'),
    # http://127.0.0.1:7000/blog/2025/01/post-1/
    re_path(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/$',
        post_detail,
        name='blog_post_detail'),
]
