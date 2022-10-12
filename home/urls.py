from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('QuiSommesNous/', views.about, name='about'),
    path('', views.home, name='home'),
]

