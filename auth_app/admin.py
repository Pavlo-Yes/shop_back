from django.contrib import admin

# Register your models here.
from products.models import ProductModel
from user.models import UserModel

admin.site.register(UserModel)
admin.site.register(ProductModel)
