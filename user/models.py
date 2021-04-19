from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    id = models.AutoField(primary_key=True)

    # product_id = models.CharField(max_length=20, default='', blank=True)
    # email = models.EmailField(max_length=50, unique=True)
