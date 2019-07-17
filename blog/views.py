from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

from blog.models import Post

# Create your views here.

def posts(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/posts.html', context={ 'posts': posts })

@staff_member_required
def edit_post(request, **kwargs):
    post_id = kwargs['id']
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/edit.html', context={ 'post': post })