from django.urls import path
from . import views

urlpatterns = [
    path('', views.boutique, name='boutique'),
]

