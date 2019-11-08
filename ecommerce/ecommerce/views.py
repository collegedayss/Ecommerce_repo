from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        'title': "Home Page"
    }
    return render(request, "home_page.html", context)


def about_page(request):
        context = {
        'title': "ABOUT Page"
    }
    return render(request, "home_page.html", {})


def contact_page(request):
        context = {
        'title': "CONTACT Page"
    }
    return render(request, "home_page.html", {})
