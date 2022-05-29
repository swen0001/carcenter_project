from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    class Meta:
        db_table = 'auth_user'


    USERNAME_FIELD = 'email'
    email = models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address')
    REQUIRED_FIELDS = []

