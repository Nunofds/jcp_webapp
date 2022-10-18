from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('profil/<username>', views.user_home, name='user_home'),
    path('MettreAjour/<username>', views.user_update_profil, name='update_profil'),
    path('SupprimerCompte/<username>', views.user_delete_profil, name='delete_profil'),
]

