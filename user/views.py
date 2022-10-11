from django.contrib.auth.decorators import login_required
from account.forms import InscriptionForm
from django.shortcuts import render


@login_required()
def user_home(request):
    context = {}
    return render(request, 'user/user_home.html', context)


@login_required()
def user_reservation(request):
    context = {}
    return render(request, 'user/reservations.html', context)


@login_required()
def user_update_profil(request):
    form = InscriptionForm

    context = {'form': form}
    return render(request, 'user/update_profil.html', context)
