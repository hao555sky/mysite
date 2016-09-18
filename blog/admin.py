from django.contrib import admin

from .models import Category, Blog


# Register your models here.
admin.site.register(Category)


# 添加Tinymce编辑器
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ['blog/tinymce/js/tinymce/tinymce.min.js',
              'blog/tinymce/config.js']

admin.site.register(Blog, BlogAdmin)