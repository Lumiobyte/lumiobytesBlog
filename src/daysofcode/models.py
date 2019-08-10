from django.db import models
from django.utils import timezone

class DayLog(models.Model):

    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    day = models.CharField(max_length=20)
    dayInternal = models.IntegerField()

    add_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:

        ordering = ['-id']