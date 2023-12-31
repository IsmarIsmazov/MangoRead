from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.users.manager import CustomUserManager


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='media/avatars/', blank=True, null=True, verbose_name='image_user')
    date_of_birth = models.DateField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    nickname = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/avatars/', blank=True, null=True, verbose_name='Profiles_avatar')
