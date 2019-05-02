from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_booking, name='view-booking'),
    path('search/', views.search, name='search'),
    path('book/', views.book, name='book'),
]
