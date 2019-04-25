from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from users.models import Passenger

from .models import Booking, Wallet


@receiver(post_save, sender=Passenger)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(passenger=instance)


@receiver(post_save, sender=Passenger)
def save_wallet(sender, instance, **kwargs):
    instance.wallet.save()


@receiver(post_save, sender=Booking)
def decrement_seats(sender, instance, **kwargs):
    instance.train.seats_remaining -= instance.seats_booked
    instance.train.save()


@receiver(post_delete, sender=Booking)
def increment_seats(sender, instance, **kwargs):
    instance.train.seats_remaining += instance.seats_booked
    instance.train.save()
