from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name