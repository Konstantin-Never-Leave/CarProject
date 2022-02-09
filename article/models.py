from django.db import models
from django.conf import settings
from django.urls import reverse

from account.models import *


class Author(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='author')
    article = models.ForeignKey("Article", on_delete=models.PROTECT, related_name='article_id')


class Article(models.Model):

    title = models.CharField("Brand", max_length=50)
    heading = models.CharField("Model", max_length=50)
    slug = models.SlugField(max_length=40, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField("Description")
    image = models.ImageField(upload_to="photo/%Y/%m/%d", verbose_name="Image")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    time_public = models.BooleanField(default=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.PROTECT,
                               verbose_name="Category",
                               related_name='author_of_article')

    class Meta:
        verbose_name = ''

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('car_model_url', kwargs={'car_model_slug': self.slug})
