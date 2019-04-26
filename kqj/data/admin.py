from django.contrib import admin

# Register your models here.
from .models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['id','name','text']