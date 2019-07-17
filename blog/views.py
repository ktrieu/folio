from django.shortcuts import render
from blog.models import Post

# Create your views here.

def posts(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/posts.html', context={ 'posts': posts })