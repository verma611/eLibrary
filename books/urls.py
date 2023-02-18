from django.urls import path
from . import views

app_name= 'books'

urlpatterns = [
    path('', views.HomePage, name='index'),
    path('books', views.index, name='HomePage'),
    path('Search', views.Search, name='Search'),
    path('DisplayBook', views.DisplayBook, name='DisplayBook'),
]