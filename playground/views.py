from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    # return render(request, 'hello.html', {'name': 'Nada'})
    return HttpResponse("<h1>Hello Nada!</h1>")

def about_page(request):
    return HttpResponse("<h1>About us!</h1>")

def contact_page(request):
    return HttpResponse("<h1>Contact us!</h1>")
