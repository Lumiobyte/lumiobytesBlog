from django.db import models
from django.conf import settings
from django.db.models import Q
from django.utils import timezone

# Create your models here.
User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
    def search(self, query):
        lookup = Q(title__icontains=query) | Q(content__icontains=query) | Q(slug__icontains=query)

        return self.filter(lookup)

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if not query:
            return self.get_queryset().none()
        
        return self.get_queryset.search(query)

class BlogPost(models.Model):

    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)

    slug = models.SlugField(unique = True)
    title = models.CharField(max_length = 120)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    content = models.TextField(null = True, blank = True)
    add_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = BlogPostManager()

    class Meta:
        ordering = ['-add_timestamp', '-edited_date']