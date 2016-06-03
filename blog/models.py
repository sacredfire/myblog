from django.db import models
from django.utils import timezone


class Post(models.Model):
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def __str__(self):
        return self.title
