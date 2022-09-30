from django.shortcuts import render


def reservation(request):
    return render(request, 'reservation/reservation.html')

