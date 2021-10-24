from django.db import models
from datetime import datetime
# Create your models here.


class Event(models.Model):
    title = models.TextField()
    description = models.TextField(default=None)
    date = models.DateField(null=True, blank=True, default=None)
    img = models.ImageField(upload_to='pics')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

