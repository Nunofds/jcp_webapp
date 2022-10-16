from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation


@login_required()
def user_reservation(request, pk=None):
    reservations = Reservation.objects.all()
    total_reservations = reservations.count()

    context = {
        'reservations': reservations,
        'total_reservations': total_reservations
    }
    return render(request, 'reservation/reservations.html', context)


@login_required()
def user_new_reservation(request, pk=None):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            pc = Reservation(
                fullName=cd['fullName'],
                adress=cd['adress'],
                zip_code=cd['zip_code'],
                city=cd['city'],
                email=cd['email'],
                phone=cd['phone'],
                date=cd['date'],
                hour=cd['hour'],
                message=cd['message'],
            )
            pc.save()
            messages.success(request, 'Votre réservation a bien été envoyé!')
            return redirect('reservation:user_reservation')
    else:
        form = ReservationForm

    context = {'form': form}
    return render(request, 'reservation/new_reservation.html', context)


def user_update_reservation(request, pk):
    reservation_id = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservation_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre réservation a bien été modifé!')
            return redirect('reservation:user_reservation')

    context = {'form': form}
    return render(request, 'reservation/new_reservation.html', context)


def user_delete_reservation(request, pk=None):
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation:user_reservation')

    context = {'reservation': reservation}
    return render(request, 'reservation/delete_reservation.html', context)
