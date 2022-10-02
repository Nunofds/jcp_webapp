from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from .forms import inscriptionForm


def inscription(request):
    if request.user.is_authenticated:
        return redirect('user_home')

    if request.method == 'POST':
        form = inscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Nouvelle compte crée: {user.username}")
            return redirect('account:connexion')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = inscriptionForm()

    context = {'form': form}
    return render(request, 'account/inscription.html', context)


def connexion(request):
    context = {}
    return render(request, 'account/connexion.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def rgpd(request):
    context = {}
    return render(request, 'account/rgpd.html', context)

