from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .decorators import user_not_authenticated
from django.contrib import messages
from .forms import InscriptionForm, UserLoginForm


@user_not_authenticated()
def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Nouvelle compte crée: {user.username}")
            return redirect('user:user_home')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = InscriptionForm()

    context = {'form': form}
    return render(request, 'account/inscription.html', context)


@user_not_authenticated()
def connexion(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenue <b>{user.username}</b>! Vous avez été connecté!")
                return redirect("user:user_home")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = UserLoginForm()

    context = {"form": form}
    return render(request, "account/connexion.html", context)


@login_required()
def logout_user(request):
    logout(request)
    messages.info(request, "Vous êtes bien déconnecté!")
    return redirect('account:connexion')


def rgpd(request):
    context = {}
    return render(request, 'account/rgpd.html', context)

