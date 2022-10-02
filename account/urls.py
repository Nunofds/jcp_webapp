from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.logout_user, name='logout'),
    path('rgpd/', views.rgpd, name='rgpd'),
    path('meConnecter/', views.connexion, name='connexion'),
    path('m\'inscrire/', views.inscription, name='inscription'),
]
