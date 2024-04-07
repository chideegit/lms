from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    is_educator = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    
