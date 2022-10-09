from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from account.my_captcha import FormWithCaptcha


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid() and request.POST.get('g-recaptcha-response'):
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = ['fernandes.n.sa@outlook.fr', 'n.b.fernandes@outlook.fr']

            send_mail(subject, message, email, recipients)
            messages.success(request, f"Merci <b>{name}</b> ! Votre message a bien été envoyé.")
            return redirect('contact:contact')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        if not request.POST.get('g-recaptcha-response'):
            messages.error(request, "Ce champs est oblifatoire!")
    else:
        form = ContactForm

    captcha = FormWithCaptcha

    content = {'form': form, 'captcha': captcha, }
    return render(request, 'contact/contact.html', content)
