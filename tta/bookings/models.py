from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from users import views as user_views
from users.models import Passenger


class Wallet(models.Model):
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
    balance = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = 'Wallet'

    def __str__(self):
        return f'{self.passenger.username} Wallet'


class Train(models.Model):
    train_no = models.IntegerField(
        verbose_name='Train Number',
    )

    train_name = models.CharField(
        verbose_name='Train Name',
        max_length=30,
    )

    source = models.CharField(
        verbose_name='Source',
        max_length=30,
    )

    destination = models.CharField(
        verbose_name='Destination',
        max_length=30,
    )

    seats_remaining = models.IntegerField(
        verbose_name='# of seats remaining',
        validators=[MinValueValidator(0)],
    )

    departure_time = models.TimeField(
        verbose_name='Departure time',
    )

    travel_time = models.DurationField(
        verbose_name='Travel time'
    )

    fare = models.IntegerField(
        verbose_name='Fare',
        validators=[MinValueValidator(100)],
    )

    class Meta:
        verbose_name = 'Train'

    def __str__(self):
        return self.train_name


class Booking(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)

    date = models.DateField(
        verbose_name='Travel Date',
        default=timezone.now,
    )

    pnr_no = models.CharField(
        verbose_name='PNR Number',
        max_length=10,
    )

    seats_booked = models.IntegerField(
        verbose_name='# of seats booked',
        validators=[MinValueValidator(1)],
    )

    class Meta:
        verbose_name = 'Booking'

    def __str__(self):
        return f'{self.passenger.username} - #{self.pnr_no}'
