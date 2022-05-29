from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser


class MyUserAdmin(UserAdmin):
    model = MyUser


admin.site.register(MyUser, MyUserAdmin)
