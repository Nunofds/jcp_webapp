from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from user.forms import Update_profile


@login_required(login_url='user:user_home')
def user_home(request, pk=None):
    context = {}
    return render(request, 'user/user_home.html', context)


@login_required()
def user_update_profil(request, pk=None):
    user = User.objects.get(id=pk)
    form = Update_profile(instance=user)
    if request.method == 'POST':
        form = Update_profile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:update_profil', pk=request.user.id)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    context = {'form': form}
    return render(request, 'user/update_profil.html', context)


@login_required(login_url='user:delete_profil')
def user_delete_profil(request, pk=None):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Votre compte a bien été supprimé !')
        return redirect('home:home')
    context = {'user': user}
    return render(request, 'user/delete_profil.html', context)

