from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Wallet
from users.models import Passenger


@receiver(post_save, sender=Passenger)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(passenger=instance)


@receiver(post_save, sender=Passenger)
def save_wallet(sender, instance, **kwargs):
    instance.wallet.save()
