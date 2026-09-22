from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title