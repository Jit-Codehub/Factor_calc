from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class category(models.Model):
    sub_name=models.CharField(max_length=200)
    def __str__(self):
        return self.sub_name
class Differ(models.Model):
    slug=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    header=models.CharField(max_length=200)
    subject=models.ForeignKey(category,max_length=200,on_delete=models.CASCADE)
    sub_subject=models.CharField(max_length=200)
    content=RichTextUploadingField()
    def __str__(self):
        return self.slug
