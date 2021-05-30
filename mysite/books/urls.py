
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.start_page),
    path('index/', views.all_books, name = 'index')
]