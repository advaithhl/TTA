from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_booking, name='view-booking'),
    path('new/', views.new_booking, name='new-booking'),
]
