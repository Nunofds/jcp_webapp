from django.contrib.auth import login, logout, authenticate, get_user_model
from django.db.models import Q
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import InscriptionForm, UserLoginForm, SetNewPasswordForm, ResetPasswordForm
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from .decorators import user_not_authenticated
from django.shortcuts import render, redirect
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from .my_captcha import FormWithCaptcha
from django.contrib import messages


# validate inscription by link send to email
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, f"Merci pour votre e-mail de confirmation. Vous pouvez maintenant vous connecter \
        à votre compte.")
        return redirect('my_account:connexion')
    else:
        messages.error(request, "Le lien d'activation est invalide!")

    return redirect('my_account:connexion')


# function with the message, to send an email after inscription
def activateEmail(request, user, to_email):
    mail_subject = "Activez votre compte utilisateur."
    message = render_to_string(
        'account/template_activate_account.html', {
            'user': user.username,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            'protocol': 'https' if request.is_secure() else 'http',
        }
    )
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Cher <b>{user}</b>, veuillez accéder à votre boîte de réception <b>{to_email}</b> et \
                                    cliquer sur le lien d\'activation reçu pour confirmer et terminer l\'inscription. \
                                    <b>Remarque:</b> vérifiez votre dossier spam.')
        return redirect('my_account:connexion')
    else:
        messages.error(request, f"Problème d'envoi de l'e-mail de confirmation à {to_email}, vérifiez si vous l'avez \
                                tapé correctement.")


# users inscription
@user_not_authenticated
def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid() and request.POST.get("g-recaptcha-response"):
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))

            # messages.success(request, f"Nouveau compte crée pour: {user.username}")
            # return redirect('my_account:connexion')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        if not request.POST.get("g-recaptcha-response"):
            messages.error(request, 'Le champ CAPTCHA est obligatoire!')

    else:
        form = InscriptionForm()

    context = {'form': form, 'captcha': FormWithCaptcha}
    return render(request, 'account/inscription.html', context)


# users connexion
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

        if not request.POST.get("g-recaptcha-response"):
            messages.error(request, 'Le champ CAPTCHA est obligatoire!')

    form = UserLoginForm()
    captcha = FormWithCaptcha

    context = {"form": form, 'captcha': captcha}
    return render(request, "account/connexion.html", context)


# Passsword change for users
@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetNewPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"""<b>{user.username}</b> Votre mot de passe a bien été modifié! <br>
                                        Veuillez vous reconnecter! """)
            return redirect('my_account:connexion')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = SetNewPasswordForm(user)

    context = {'form': form}
    return render(request, 'account/password_change.html', context)


# Password reset for users
@user_not_authenticated
def password_reset(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid() and request.POST.get("g-recaptcha-response"):
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Récupération du mot de passe"
                message = render_to_string(
                    'account/template_reset_password.html', {
                        'user': associated_user.username,
                        'domain': get_current_site(request).domain,
                        'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                        'token': account_activation_token.make_token(associated_user),
                        'protocol': 'https' if request.is_secure() else 'http',
                    }
                )
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request, """
                                                <p>Réinitialisation du mot de passe envoyée</h2><hr>
                                                <p>
                                                    Nous vous avons envoyé par e-mail des instructions pour définir \
                                                    votre mot de passe.
                                                    <br>
                                                    Si vous ne recevez pas d'e-mail, assurez-vous d'avoir saisi le bon \
                                                    adresse e-mail.
                                                    <br>
                                                    Vérifiez votre dossier spam.
                                                </p>
                                                """)
                else:
                    messages.error(request, f""" Problème d'envoi de l'e-mail de réinitialisation du mot de passe, \
                                                <b>PROBLÈME DE SERVEUR</b> """)
            return redirect('my_account:connexion')

        if not request.POST.get("g-recaptcha-response"):
            messages.error(request, 'Le champ CAPTCHA est obligatoire!')

    form = ResetPasswordForm()
    captcha = FormWithCaptcha

    context = {
        'form': form,
        'captcha': captcha
    }
    return render(request, 'account/password_reset.html', context)


# Confirm password reset for users (template)
@user_not_authenticated
def password_reset_confirm(request, uidb64, token):
    context = {}
    return render(request, 'account/rgpd.html', context)


# users logout
@login_required
def logout_user(request):
    logout(request)
    messages.info(request, "Vous êtes bien déconnecté!")
    return redirect('my_account:connexion')


# rgpd page
def rgpd(request):
    context = {}
    return render(request, 'account/rgpd.html', context)
