from django.urls import path
from . import views

urlpatterns = [
    path('a_propos/', views.about),
    path('', views.home),
]

