from django.db.models.signals import post_save
from .models import Passenger, Profile
from django.dispatch import receiver


@receiver(post_save, sender=Passenger)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(passenger=instance)


@receiver(post_save, sender=Passenger)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
