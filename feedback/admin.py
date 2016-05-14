from django.contrib import admin
from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('subject', 'author', 'timestamp', 'feedback_type')
    list_filter = ('feedback_type',)
    raw_id_fields = ["author", ]
    search_fields = ('body', "subject")

admin.site.register(Feedback, FeedbackAdmin)
