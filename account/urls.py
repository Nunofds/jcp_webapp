from django.urls import path
from . import views

app_name = 'my_account'

urlpatterns = [
    path('deconnexion/', views.logout_user, name='logout'),
    path('rgpd/', views.rgpd, name='rgpd'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('changer_password/', views.password_change, name='password_change'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('reset/<uidb64>/<token>', views.password_reset_confirm, name='password_reset_confirm'),
]
