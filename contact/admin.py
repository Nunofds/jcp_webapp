from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'message')
    search_fields = ['name']


admin.site.register(Contact, ContactAdmin)

