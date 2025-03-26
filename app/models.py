from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Counter(models.Model):
    date = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.date


class Announcement(models.Model):
    content = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
