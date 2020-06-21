"""novels models."""
from django.db import models


class Novel(models.Model):
    """novel model."""
    name = models.CharField(max_length=16, unique=True)
    author = models.CharField(max_length=8)
    rank = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    comment = models.IntegerField(default=0, help_text='number of comments.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
