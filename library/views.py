from django.shortcuts import render

from books.models import Book


def home(request):
    return render(request, "home.html",
                  {'week_specials': Book.objects.get_recommended()})
