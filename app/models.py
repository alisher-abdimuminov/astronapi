from django.db import models


class Counter(models.Model):
    date = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.date
