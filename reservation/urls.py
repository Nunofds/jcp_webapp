from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('', views.user_reservation, name='user_reservation'),
    path('nouvelleReservation', views.user_new_reservation, name='user_new_reservation'),
    path('MiseAjour/<str:pk>', views.user_update_reservation, name='user_update_reservation'),
    path('Supprimer/<str:pk>', views.user_delete_reservation, name='user_delete_reservation'),
]

