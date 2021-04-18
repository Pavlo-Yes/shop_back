from django.db import models

from user.models import UserModel


class ProductModel(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500)
    price = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=50)
    sold_out = models.BooleanField(default=False)
    likes = models.PositiveSmallIntegerField(default=0, blank=True)
    photos = models.FileField(blank=True, default='')

# class ProductPhotos(models.Model):
#     photo = models.FileField(upload_to=os.path.join('Products', 'img'), default='', blank=True)
#     product = models.ForeignKey(ProductModel, default='', on_delete=models.SET_DEFAULT, related_name='photos')
