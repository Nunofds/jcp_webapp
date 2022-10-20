from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .decorators import user_not_authenticated
from django.contrib import messages
from .forms import InscriptionForm, UserLoginForm
from .my_captcha import FormWithCaptcha


@user_not_authenticated
def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid() and request.POST.get("g-recaptcha-response"):
            user = form.save()
            messages.success(request, f"Nouveau compte crée pour: {user.username}")
            return redirect('my_account:connexion')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = InscriptionForm()

    context = {'form': form, 'captcha': FormWithCaptcha}
    return render(request, 'account/inscription.html', context)


@user_not_authenticated
def connexion(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid() and request.POST.get("g-recaptcha-response"):
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenue {user.username} ! Vous êtes connecté!")
                return redirect("user:user_home", request.user.username)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = UserLoginForm()
    captcha = FormWithCaptcha

    context = {"form": form, 'captcha': captcha}
    return render(request, "account/connexion.html", context)


@login_required
def logout_user(request):
    logout(request)
    messages.info(request, "Vous êtes bien déconnecté!")
    return redirect('my_account:connexion')


def rgpd(request):
    context = {}
    return render(request, 'account/rgpd.html', context)
