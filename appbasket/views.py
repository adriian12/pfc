from django.shortcuts import render


def noticias(request):
    return render(request, 'squadbasket/noticias.html', {})
