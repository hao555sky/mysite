from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)
    url = models.CharField(max_length=200)
    create_time = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', args=[self.name])


class Blog(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=20)
    content = models.TextField()
    summary = models.CharField(max_length=200, default="No Sumaary")
    tags = models.CharField(max_length=200, default="未分类")
    img = models.ImageField(default="")
    create_time = models.DateField(default="2012-01-01")
    views = models.IntegerField(default=0, verbose_name='people who views')

    def __str__(self):
        return self.title

    def get_tags(self):
        tagslist = self.tags.split(',')
        return tagslist

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id])

