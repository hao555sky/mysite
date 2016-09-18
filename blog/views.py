from django.shortcuts import render
from django.views import generic
from django.views.generic.base import ContextMixin

from .models import Category, Blog


# Create your views here.
class BaseMixIn(generic.ListView):
    def get_context_data(self, **kwargs):
        context = super(BaseMixIn, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class IndexView(BaseMixIn):
    template_name = 'blog/index.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['bloglists'] = Blog.objects.all()
        return context


class AllView(BaseMixIn):
    template_name = 'blog/all.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(AllView, self).get_context_data(**kwargs)
        context['bloglists'] = Blog.objects.all()
        return context


class CategoryView(BaseMixIn):
    template_name = 'blog/all.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        key = self.kwargs.get('category')
        context['bloglists'] = Blog.objects.filter(category__name=key)
        return context


class BlogView(BaseMixIn):
    template_name = 'blog/detail.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        blogId = self.kwargs.get('blogId')
        # context['blog'] = Blog.objects.get(id=blogId)
        context['error'] = blogId
        return context
