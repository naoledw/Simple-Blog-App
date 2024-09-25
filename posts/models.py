from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
