from django.shortcuts import render, redirect
from .forms import inscriptionForm


def inscription(request):
    form = inscriptionForm()
    if request.method == 'POST':
        form = inscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    context = {'form': form}
    return render(request, 'account/inscription.html', context)


def connexion(request):
    context = {}
    return render(request, 'account/connexion.html', context)
