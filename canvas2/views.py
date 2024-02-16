from django.shortcuts import render


def index(request):
    return render(request, "canvas2/index.html")
