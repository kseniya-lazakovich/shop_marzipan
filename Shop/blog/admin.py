from django.contrib import admin
from .models import Post, Comment, Section

@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'slug']
    list_filter = ['created']
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment) 
class CommentAdmin(admin.ModelAdmin):    
    list_display = ('name', 'email', 'post', 'created', 'active')    
    list_filter = ('active', 'created', 'updated')    
    search_fields = ('name', 'email', 'body') 

admin.site.register(Section)