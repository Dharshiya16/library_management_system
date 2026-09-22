from django.db import models
from books.models import Book
from members.models import Member


class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.book.title} - {self.member.name}"