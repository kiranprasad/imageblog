from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.TextField()
    content=models.TextField()
    tags=models.TextField()
    url=models.URLField()
    votes=models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField()
    votes = models.IntegerField(default=0)
    posted_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content
