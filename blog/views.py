from django.db.models import Q
from django.views import generic
import logging

from .models import Category, Blog


# Create your views here.
class BaseMixIn(generic.ListView):
    def get_context_data(self, **kwargs):
        context = super(BaseMixIn, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['hotblogs'] = Blog.objects.order_by('-views')[:5]
        return context


class IndexView(BaseMixIn):
    template_name = 'blog/index.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['bloglists'] = Blog.objects.all()
        return context


class AllView(BaseMixIn):
    template_name = 'blog/all.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(AllView, self).get_context_data(**kwargs)
        context['bloglists'] = Blog.objects.all()
        return context


class CategoryView(BaseMixIn):
    template_name = 'blog/all.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        logging.debug('categoryView')
        key = self.kwargs.get('category')
        context['bloglists'] = Blog.objects.filter(category__name=key)
        return context


class BlogView(BaseMixIn, generic.DetailView):
    template_name = 'blog/detail.html'
    model = Blog

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super(BlogView, self).get_context_data(**kwargs)
        blogId = self.kwargs.get('pk')
        blog = Blog.objects.get(id=blogId)
        blog.views += 1
        blog.save()
        context['blog'] = blog
        return context


class SearchView(BaseMixIn):
    template_name = 'blog/all.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        key = self.request.GET.get('search')
        context['bloglists'] = Blog.objects.filter(Q(title__icontains = key) | Q(tags__icontains = key))
        return context