from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import BookList
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created {username}")
            login(request, user)
            return redirect(start_page)
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="main/register.html",
                          context={"form": form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "books/register.html",
                  context={"form": form})
