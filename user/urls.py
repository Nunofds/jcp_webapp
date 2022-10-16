from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('profil/<str:pk>', views.user_home, name='user_home'),
    path('MettreAjour/<str:pk>', views.user_update_profil, name='update_profil'),
    path('SupprimerCompte/<str:pk>', views.user_delete_profil, name='delete_profil'),
]

