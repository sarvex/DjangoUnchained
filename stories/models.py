# coding=utf-8
from urllib.parse import urlparse

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    points = models.IntegerField()
    moderator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def domain(self):
        return urlparse(self.url).netloc

    def __unicode__(self):
        return self.title
