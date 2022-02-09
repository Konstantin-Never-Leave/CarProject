# from django.db import models
# from django.conf import settings
# from django.urls import reverse
#
# from account.models import *
#
#
# class Brand(models.Model):
#     brand = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='brand')
#     slug = models.SlugField("URL", on_delete=models.PROTECT, related_name='brand_url')
#     country = models.CharField('produced_in', max_length=50)
#
#
# class Car(models.Model):
#
#     model = models.CharField("model", max_length=50)
#     content = models.TextField("description")
#     slug = models.SlugField(max_length=40, unique=True, db_index=True, verbose_name="car_url")
#     x = models.TextField("Description")
#     image = models.ImageField(upload_to="photo/%Y/%m/%d", verbose_name="Image")
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     time_public = models.BooleanField(default=True)
#     reviewed_by = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                on_delete=models.PROTECT,
#                                verbose_name="Category",
#                                related_name='car_added_by')
#     added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                on_delete=models.PROTECT,
#                                verbose_name="Category",
#                                related_name='car_added_by')
#
#     class Meta:
#         verbose_name = ''
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('car_model_url', kwargs={'car_model_slug': self.slug})