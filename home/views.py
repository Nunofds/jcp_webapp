from django.shortcuts import render


def home(request):
    return render(request, "home/home.html")


def about(request):
    return render(request, 'home/about.html')


def error_404(request, exception):
    return render(request, '404.html')
