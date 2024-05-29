from datetime import date
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class AppUserManager(BaseUserManager):
    def create_user(
            self,
            email,
            password=None,
            first_name=None,
            last_name=None,
            date_of_birth=None,
            sex=None,
            user_bio=None,
            user_type=None,
            is_active=False,
    ):
        if not email:
            raise ValueError("An Email is required")
        if not password:
            raise ValueError("A Password is required")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            sex=sex,
            user_bio=user_bio,
            user_type=user_type,
            is_active=is_active,
        )
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
        user.is_staff = True
        user.save()
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('producer', 'Producer'),
        ('talent', 'Talent'),
    )

    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=55, null=True, blank=True)
    user_bio = models.TextField(null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()

    @property
    def age(self):
        if self.date_of_birth is None:
            return None
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


class UserAddress(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    address_line_one = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip = models.CharField(max_length=50, null=True, blank=True)


class SocialMediaAccounts(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    account_title = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(unique=True, null=True, blank=True)
