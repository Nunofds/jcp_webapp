from django.urls import path
from . import views
from django.conf.urls import handler404

app_name = 'home'

urlpatterns = [
    path('QuiSommesNous/', views.about, name='about'),
    path('', views.home, name='home'),
]


handler404 = "home.views.error_404"
