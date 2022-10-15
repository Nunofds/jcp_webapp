from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('', views.user_reservation, name='user_reservation'),
    path('nouvelleReservation', views.user_new_reservation, name='user_new_reservation'),
]

