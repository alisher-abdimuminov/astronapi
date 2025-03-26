from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Counter(models.Model):
    date = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.date
    
    class Meta:
        verbose_name = "Sanagich"
        verbose_name_plural = "Sanagichlar"


class Announcement(models.Model):
    content = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name = "E'lon"
        verbose_name_plural = "E'lonlar"
