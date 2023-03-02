from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name="blog_posts")
                              
    body = models.TextField()
    
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2,
                             choices=Status.choices,
                             default=Status.DRAFT)
    
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    objects = models.Manager() # The default manager
    published = PublishedManager() # Our custom manager


    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"])
        ]

    
    def get_absolute_url(self):

        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):

        return self.title
