from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=None, null=True)
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
