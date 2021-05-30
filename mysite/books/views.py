from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import BookList


def start_page(request):
    return render(
        request,
        'books/start_page.html',
        {}

    )

def all_books(request):
    lists = BookList.objects.all()
    return render(
        request,
        'books/all_books.html',
        {'all_books': lists}
    )
