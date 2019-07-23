import datetime
import os

from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify

from markdown2 import Markdown
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()

    markdown_content = models.TextField(blank=True)
    html_content = models.TextField(blank=True)

    published = models.BooleanField(default=False)
    publish_date = models.DateTimeField(blank=True, null=True)

    last_edit_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            #this is a create not a update
            self.slug = slugify(self.title)
        #compile the markdown
        self.html_content = Markdown().convert(self.markdown_content)
        self.last_edit_date = datetime.datetime.now()
        super(Post, self).save()

    class Meta:
        ordering = ['-publish_date']

def get_image_path(instance, filename):
    media_dir = settings.MEDIA_ROOT
    post_dir = instance.post.slug
    path = os.path.join(media_dir, post_dir, instance.name)
    #fix extension to match the extenions of the uploaded file
    _, ext = os.path.splitext(filename)
    name, _ = os.path.splitext(path)
    return name + ext


class PostImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_image_path)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)