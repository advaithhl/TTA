from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Passenger(User):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    age = models.IntegerField(
        verbose_name='Age',
        validators=[MinValueValidator(18)],
    )

    gender = models.CharField(
        verbose_name='Gender',
        max_length=1,
        choices=GENDER_CHOICES,
    )

    address = models.CharField(
        verbose_name='Address',
        max_length=300,
    )

    phone_no = models.CharField(
        verbose_name='Phone',
        max_length=16,
    )

    class Meta:
        verbose_name = 'Passenger'


class Profile(models.Model):
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Profile'

    def __str__(self):
        return f'{self.passenger.username} Profile'
