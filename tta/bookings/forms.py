from datetime import date, timedelta

from django import forms
from django.core.exceptions import ValidationError

from .models import Booking, Train


class SearchForm(forms.Form):
    source = forms.CharField(
        label='Source',
        max_length=30,
    )
    destination = forms.CharField(
        label='Destination',
        max_length=30,
    )
    date = forms.DateField(
        label='Date',
    )

    def clean_date(self):
        cd = self.cleaned_data
        booking_date = cd.get('date')
        if booking_date < date.today() + timedelta(days=1):
            raise ValidationError('This date has already passed!')

        return cd
