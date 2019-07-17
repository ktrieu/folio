from django.shortcuts import render
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
    return HttpResponse(post_id)