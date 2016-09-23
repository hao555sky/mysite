from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^all/$', views.AllView.as_view(), name='all'),
    url(r'^me/$', views.MeView.as_view(), name='me'),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^(?P<pk>\d+)/$', views.BlogView.as_view(), name='detail'),
    url(r'^(?P<category>\w+)/$', views.CategoryView.as_view(), name='category'),
    # if this line exchanges the location with last line, the third line will not map the BlogView correctly.

]