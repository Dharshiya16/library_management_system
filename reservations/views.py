from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

def reservation_list(request):

    search = request.GET.get('search', '')

    reservations = Reservation.objects.filter(
        book__title__icontains=search
    ) | Reservation.objects.filter(
        member__name__icontains=search
    )

    return render(
        request,
        'reservations/reservation_list.html',
        {
            'reservations': reservations,
            'search': search
        }
    )


def reservation_add(request):

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('reservation_list')

    else:
        form = ReservationForm()

    return render(
        request,
        'reservations/reservation_form.html',
        {'form': form}
    )
def reservation_delete(request, id):

    reservation = Reservation.objects.get(id=id)
    reservation.delete()

    return redirect('reservation_list')
def reservation_edit(request, id):

    reservation = Reservation.objects.get(id=id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)

        if form.is_valid():
            form.save()
            return redirect('reservation_list')

    else:
        form = ReservationForm(instance=reservation)

    return render(
        request,
        'reservations/reservation_form.html',
        {'form': form}
    )
