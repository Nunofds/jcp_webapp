from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'city', 'date', 'hour', 'message', 'accepted')
    search_fields = ['fullName']


admin.site.register(Reservation, ReservationAdmin)
