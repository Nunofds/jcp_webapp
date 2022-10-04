from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.user_home, name='user_home'),
    path('mesReservations', views.user_reservation, name='user_reservation'),
]

