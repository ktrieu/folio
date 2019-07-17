from django.shortcuts import render
from blog.models import Post
from django.http.response import HttpResponse

# Create your views here.

def posts(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/posts.html', context={ 'posts': posts })

def edit_post(request, **kwargs):
    post_id = kwargs['id']
    return HttpResponse(post_id)