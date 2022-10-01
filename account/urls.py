from django.urls import path
from . import views

urlpatterns = [
    path('m\'inscrire/', views.inscription, name='inscription'),
    path('me_connecter/', views.connexion, name='connexion'),
]
