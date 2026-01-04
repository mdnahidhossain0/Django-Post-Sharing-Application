from django.contrib import admin
from .models import Tweet


class TweetAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at')
    search_fields = ('author__username', 'content')

admin.site.register(Tweet, TweetAdmin)