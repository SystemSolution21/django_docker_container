from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE

from .models import HomePageContent


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }
    list_display = ("title", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "content")
