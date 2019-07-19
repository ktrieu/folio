import datetime

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