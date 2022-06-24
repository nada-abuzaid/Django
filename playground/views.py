from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    my_name = 'Nada!'
    return render(request, 'hello.html', {'name': my_name})


def about_page(request):
    return HttpResponse("<h1>About us!</h1>")


def contact_page(request):
    return HttpResponse("<h1>Contact us!</h1>")
