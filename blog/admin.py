from django.contrib import admin
from blog.models import Post
from django.utils.html import format_html

def post_edit_link(post):
    return format_html(f'<a href=/blog/edit/{post.id}/>Edit</a>')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    prepopulated_fields = { 'slug': ('title',)}
    list_display = ['title', post_edit_link]
