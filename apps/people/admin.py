from django.contrib import admin
from people.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('username', 'first_name', 'last_name',)
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(UserProfile, UserProfileAdmin)
