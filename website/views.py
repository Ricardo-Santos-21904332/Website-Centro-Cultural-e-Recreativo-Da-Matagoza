from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "website/index.html")


def about(request):
    return render(request, "website/about.html")


def comida(request):
    return render(request, "website/comida.html")


def bebidas(request):
    return render(request, "website/bebidas.html")

def snacks(request):
    return render(request, "website/snacks.html")
