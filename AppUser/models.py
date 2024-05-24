from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None, user_type=None, is_active=False,):
        if not email:
            raise ValueError("An Email is required")
        if not password:
            raise ValueError("A Password is required")
        email = self.normalize_email(email)
        user = self.model(email=email, user_type=user_type, is_active=is_active)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("An Email is required")
        if not password:
            raise ValueError("A Password is required")
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save()
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('producer', 'Producer'),
        ('talent', 'Talent'),
    )
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=None)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()
