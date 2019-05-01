from datetime import date, timedelta

from django import forms
from django.core.exceptions import ValidationError

from .models import Booking, Train

increment_choices = (
    ('100', '100'),
    ('500', '500'),
    ('1000', '1000'),
    ('2000', '2000'),
)


class AddMoneyForm(forms.Form):
    amount = forms.ChoiceField(
        choices=increment_choices,
        widget=forms.RadioSelect,
    )


class SearchForm(forms.Form):
    source = forms.CharField(
        label='Source',
        max_length=30,
    )
    destination = forms.CharField(
        label='Destination',
        max_length=30,
    )
    doj = forms.DateField(
        label='Date',
    )

    def clean_doj(self):
        cd = self.cleaned_data
        booking_date = cd.get('doj')
        if booking_date < date.today() + timedelta(days=1):
            raise ValidationError('This date has already passed!')

        return booking_date
