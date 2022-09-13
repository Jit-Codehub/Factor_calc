from django.contrib.sitemaps import Sitemap
import slugify

from datetime import datetime
from django.contrib import admin

from .models import *


class Differ_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=1000
    def items(self):
        return Differ.objects.all()

    def location(self, obj):
        return '/difference-between/'+obj.slug+'/'

    def lastmod(self, obj): 
        return datetime(2022,5,10)

class Category_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=1000
    def items(self):
        return category.objects.all()

    def location(self, obj):
        return '/difference-between/'+slugify.slugify(obj.sub_name)+'/'


    def lastmod(self, obj): 
        return datetime(2022,5,10)