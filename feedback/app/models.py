from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
"""
class Post(models.Model):
    title = models.Charfield(max_length=100)
    content = models.textfield()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeighKey(User, on_delete=models.CASCADE)

"""
