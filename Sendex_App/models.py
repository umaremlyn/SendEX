# Sendex_App/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()  # Use the get_user_model function

class CustomUserManagers(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManagers()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='customuser_set',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='customuser_set',
    )

    def __str__(self):
        return self.email
        
class Shipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracking_id = models.CharField(max_length=10, unique=True)
    sender_name = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    sender_phone = models.CharField(max_length=15)
    receiver_phone = models.CharField(max_length=15)
    sender_address = models.TextField()
    receiver_address = models.TextField()
    package_size = models.CharField(max_length=20, choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# Rest of your models.py remains the same
