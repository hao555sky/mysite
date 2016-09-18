from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^all/$', views.AllView.as_view(), name='all'),
    url(r'^(?P<category>\w+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^(?P<blogId>\d+)/$', views.BlogView.as_view(), name='detail'),
]