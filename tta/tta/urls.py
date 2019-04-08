from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from bookings import views as booking_views
from users import views as user_views

urlpatterns = [
    path('', user_views.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('bookings/', include('bookings.urls')),
    path('wallet/', booking_views.wallet, name='wallet')
]
