from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def home(request):

    from books.models import Book
    from members.models import Member
    from reservations.models import Reservation

    context = {
        'book_count': Book.objects.count(),
        'member_count': Member.objects.count(),
        'reservation_count': Reservation.objects.count(),
    }

    return render(request, 'home.html', context)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('members/', include('members.urls')),
    path('reservations/', include('reservations.urls')),
]