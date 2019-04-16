from django.core.validators import MinValueValidator
from django.db import models

from users import views as user_views
from users.models import Passenger


class Wallet(models.Model):
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
    balance = models.FloatField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = 'Wallet'

    def __str__(self):
        return f'{self.passenger.username} Wallet'
