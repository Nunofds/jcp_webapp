from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def services(request):
    return HttpResponse('services page')

