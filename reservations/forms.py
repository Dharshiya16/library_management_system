from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Cancelled', 'Cancelled'),
    ]

    status = forms.ChoiceField(
        choices=STATUS_CHOICES
    )

    class Meta:
        model = Reservation
        fields = ['book', 'member', 'status']