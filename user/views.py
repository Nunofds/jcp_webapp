from django.shortcuts import render


def user_home(request):
    context = {}
    return render(request, 'user/user_home.html', context)

