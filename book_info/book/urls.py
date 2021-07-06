from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.addBook, name='add'),
    path('aboutus/', views.aboutus, name='about'),
    path('search/', views.searchBook, name='search')
]
