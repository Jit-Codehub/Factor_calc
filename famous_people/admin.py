from django.contrib import admin
from .models import *

@admin.register(FamousPeople)
class BlogAdmin(admin.ModelAdmin):
    search_fields = ["title","content"]
    exclude = ("slug",)
    list_filter = ("created_at","modified_at",)
    readonly_fields = ("jump_links","birthday_highlights","facts","created_at","modified_at",)