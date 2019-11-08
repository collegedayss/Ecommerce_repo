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
    return render(request, "home_page.html", context)


def contact_page(request):
    context = {
        'title': "CONTACT Page"
    }
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('fullname'))
    return render(request, "contact/view.html", context)
