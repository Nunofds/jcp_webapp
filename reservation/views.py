from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation


@login_required()
def user_reservation(request, pk):
    user = get_user_model().objects.get(id=pk)
    reservations = user.reservation_set.all()
    total_reservations = reservations.count()

    context = {
        'user_id': user,
        'reservations': reservations,
        'total_reservations': total_reservations
    }
    return render(request, 'reservation/reservations.html', context)


@login_required()
def user_new_reservation(request, pk):
    user = get_user_model().objects.get(id=pk)
    form = ReservationForm(initial={'user': user})

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre réservation a bien été envoyé!')
            return redirect('reservation:user_reservation', pk=request.user.id)

    context = {'form': form}
    return render(request, 'reservation/new_reservation.html', context)


@login_required()
def user_update_reservation(request, pk):
    reservation_id = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservation_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre réservation a bien été modifé!')
            return redirect('reservation:user_reservation', pk=request.user.id)

    context = {'form': form}
    return render(request, 'reservation/new_reservation.html', context)


@login_required()
def user_delete_reservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Votre réservation a bien été supprimé !')
        return redirect('reservation:user_reservation', pk=request.user.id)

    context = {'reservation': reservation}
    return render(request, 'reservation/delete_reservation.html', context)
