import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import MaxValueValidator
from datetime import date


class User(AbstractUser, PermissionsMixin):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(max_length=75, unique=True)
  bio = models.CharField(max_length=75, blank=True)
  photo = models.ImageField(blank=True, null=True)
  birthday = models.DateField(blank=True, null=True, validators=[MaxValueValidator(date.today())])
  date_joined = models.DateTimeField(auto_now_add=True)

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email']

  def __str__(self) -> str:
    return self.username