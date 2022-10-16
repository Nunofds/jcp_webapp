from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from user.forms import Update_profile


@login_required()
def user_home(request):
    context = {}
    return render(request, 'user/user_home.html', context)


@login_required()
def user_update_profil(request, pk):
    user = User.objects.get(id=pk)
    form = Update_profile(instance=user)
    if request.method == 'POST':
        form = Update_profile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:user_reservation')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    context = {'form': form}
    return render(request, 'user/update_profil.html', context)


@login_required()
def user_delete_profil(request, pk):

    context = {}
    return render(request, 'user/delete_profil.html', context)

