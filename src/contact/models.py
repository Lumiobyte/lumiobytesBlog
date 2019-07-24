from django.db import models
from django.conf import settings
from django.utils import timezone

class ContactRequests(models.Model):

    name = models.CharField(max_length = 300, null=True, blank=True)
    email = models.EmailField(max_length=120)
    content = models.TextField(null = True, blank = True)
    add_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-add_timestamp']