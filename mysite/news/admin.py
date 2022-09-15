from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('author', 'created_date', 'published_date')
    search_fields = ('title', 'text')
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ['author', 'published_date']

admin.site.register(Post, PostAdmin)