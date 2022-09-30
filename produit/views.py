from django.shortcuts import render


def boutique(request):
    return render(request, 'produit/boutique.html')

