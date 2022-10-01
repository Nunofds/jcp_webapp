from django.shortcuts import render
from .models import Services


def services(request):
    service = Services.objects.all()
    context = {'services': service}
    return render(request, 'services/services.html', context)

