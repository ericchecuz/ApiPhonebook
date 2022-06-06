from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('<int:phonebook_id>/', views.detail, name='detail'),

    path('add/', views.add, name='addphonebook'),

    path('<int:phonebook_id>/addcontact/', views.addContact, name='addcontact'),


]
