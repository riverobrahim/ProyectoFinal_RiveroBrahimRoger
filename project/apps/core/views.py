from django.shortcuts import render


def index(request):
    context = {"app_name": "VirtualPlanet"}
    return render(request, "core/index.html", context)
