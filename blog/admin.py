from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']
    list_filter = ['author', 'status', 'publish']
    search_fields = ['title', 'description']
    ordering = ['-publish', 'title']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status', )
    list_display_links = ('title',)

