from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class FamousPeople(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    subtitle = models.CharField(max_length=500,null=True,blank=True)
    meta_description = models.CharField(max_length=500,null=True,blank=True)
    jump_links = models.TextField(default="[]")
    birthday_highlights = models.TextField(default="{}")
    facts = models.TextField(default="{}")
    content = RichTextField()
    image = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(FamousPeople, self).save(*args, **kwargs)

    def __str__(self):
        return self.title