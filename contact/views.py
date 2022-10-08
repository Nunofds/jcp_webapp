from django.shortcuts import render
from .forms import ContactForm


def contact(request):

    form = ContactForm

    content = {'form':form}
    return render(request, 'contact/contact.html', content)

