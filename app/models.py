from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=240
    )
    content = models.TextField()
    creation_date = models.DateTimeField(
        auto_now_add=True
    )