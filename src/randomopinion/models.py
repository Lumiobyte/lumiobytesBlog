from django.db import models

class Opinion(models.Model):

    content = models.TextField()
    likes = models.IntegerField()
    add_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:

        ordering = ['-add_timestamp']
