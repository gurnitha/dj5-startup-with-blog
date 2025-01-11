"""suorganizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import path, include, re_path
from django.contrib import admin
from django.views.generic import (
    RedirectView, TemplateView)

from blog import urls as blog_urls
from contact import urls as contact_urls
from organizer.urls import (
    startup as startup_urls, tag as tag_urls)

urlpatterns = [
    re_path(r'^$',
        RedirectView.as_view(
            pattern_name='blog_post_list',
            permanent=False)),
    re_path(r'^about/$',
        TemplateView.as_view(
            template_name='site/about.html'),
        name='about_site'),
    path('admin/', admin.site.urls),
    re_path(r'^blog/', include(blog_urls)),
    re_path(r'^contact/', include(contact_urls)),
    re_path(r'^startup/', include(startup_urls)),
    re_path(r'^tag/', include(tag_urls)),
]
