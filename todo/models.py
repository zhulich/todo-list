from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tags")
