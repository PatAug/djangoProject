
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.start_page, name = "home"),
    path('index/', views.all_books, name = 'index'),
    path("register/", views.register, name="register"),
]