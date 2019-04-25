from django.contrib import admin

from .models import Booking, Train, Wallet

admin.site.register(Wallet)
admin.site.register(Train)
admin.site.register(Booking)
