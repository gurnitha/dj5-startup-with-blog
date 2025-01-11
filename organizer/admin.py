from django.contrib import admin

# Register your models here.

from organizer.models import Tag, Startup, NewsLink
admin.site.register(Tag)
admin.site.register(Startup)
admin.site.register(NewsLink)
