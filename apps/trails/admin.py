from django.contrib import admin
from trails.models import Trail


class TrailAdmin(admin.ModelAdmin):

    list_display = ['title', 'owner', 'created', 'urlhash']
    search_fields = ['owner', 'title', ]

admin.site.register(Trail, TrailAdmin)
