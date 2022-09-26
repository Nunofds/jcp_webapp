from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def agenda(request):
    return HttpResponse('agenda page')


