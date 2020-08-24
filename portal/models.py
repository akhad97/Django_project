from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class User(AbstractUser):
    ID_No = models.IntegerField(unique=True, validators=[MaxValueValidator(9999999999), MinValueValidator(1)])
    department = models.CharField(max_length=30, null=True, blank=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Document(models.Model):
    title = models.CharField(max_length=30, blank=False)
    document = models.FileField(upload_to='document/', blank=False)
    message = models.TextField()
    upload_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title




