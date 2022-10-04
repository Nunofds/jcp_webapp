from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required()
def user_home(request):
    context = {}
    return render(request, 'user/user_home.html', context)


@login_required()
def user_reservation(request):
    context = {}
    return render(request, 'user/reservations.html', context)
