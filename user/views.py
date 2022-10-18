from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
# from user.forms import Update_profile
from user.forms import UserUpdateProfile
from django.contrib.auth import get_user_model


@login_required(login_url='user:user_home')
def user_home(request, pk=None):
    context = {}
    return render(request, 'user/user_home.html', context)


@login_required()
def user_update_profil(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateProfile(request.POST, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, f"{user_form.username} Votre compte a bien été mis à jour!")
            return redirect('user:user_home', user_form.username)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateProfile(instance=user)
        return render(request, 'user/update_profil.html', context={'form': form})
    return redirect('user:user_home', request.user.username)


@login_required(login_url='user:delete_profil')
def user_delete_profil(request, pk=None):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Votre compte a bien été supprimé !')
        return redirect('home:home')
    context = {'user': user}
    return render(request, 'user/delete_profil.html', context)
