from django.urls import path
from . import views

app_name = 'my_account'

urlpatterns = [
    path('deconnexion/', views.logout_user, name='logout'),
    path('rgpd/', views.rgpd, name='rgpd'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
