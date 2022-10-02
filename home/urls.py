from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('a_propos/', views.about, name='about'),
    path('', views.home, name='home'),
]

