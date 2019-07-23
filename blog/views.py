from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.contrib.admin.views.decorators import staff_member_required

from markdown2 import Markdown

from blog.models import Post, PostImage

# Create your views here.
@require_GET
def posts(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/posts.html', context={ 'posts': posts })

@require_GET
@staff_member_required
def edit_post(request, **kwargs):
    post_id = kwargs['id']
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/edit.html', context={ 'post': post })

@require_POST
@staff_member_required
def render_markdown(request, **kwargs):
    markdown = Markdown()
    return HttpResponse(markdown.convert(request.body))

@require_POST
@staff_member_required
def save_markdown(request, **kwargs):
    post_id = kwargs['id']
    markdown = request.body.decode('utf-8')
    post = Post.objects.get(id=post_id)
    post.markdown_content = markdown
    post.save()
    return HttpResponse()

@require_POST
@staff_member_required
def upload_post_image(request, **kwargs):
    post_id = kwargs['id']
    post = Post.objects.get(id=post_id)
    name = request.POST.get('name')
    if not name:
        return HttpResponseBadRequest('Query parameter "name" is required.')
    image = request.FILES.get('image')
    if not image:
        return HttpResponseBadRequest('File "image" is required.')
    image = PostImage(name=name, image=image, post=post)
    image.save()
    return HttpResponse()