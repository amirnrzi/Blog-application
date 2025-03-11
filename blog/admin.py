from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'auther', 'publish', 'status']
    list_filter = ['auther', 'status', 'publish']
    search_fields = ['title', 'description']
    ordering = ['-publish', 'title']
    raw_id_fields = ['auther']
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status', )
    list_display_links = ('title',)

