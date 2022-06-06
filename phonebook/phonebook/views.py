from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets, permissions

from .models import Phonebook, Contacts
from .serializers import PhonebookSerializer, ContactsSerializer


def index(request):
    phonebooks = Phonebook.objects.all()
    template = loader.get_template('phonebook/index.html')
    context = {
        'phonebooks': phonebooks
    }
    return HttpResponse(template.render(context, request))

def detail(request, phonebook_id):
    phonebook = get_object_or_404(Phonebook, pk=phonebook_id)
    context = {
        'phonebook': phonebook
    }
    return render(request, 'phonebook/detail.html', context)

def add(request):
    phonename = request.POST['phonebook']
    var = Phonebook(name_text=phonename)
    var.save()
    response = "Phonebook %s created"
    return HttpResponse(response % phonename)

def addContact(request, phonebook_id):
    phonebook = get_object_or_404(Phonebook, pk=phonebook_id)
    name = request.POST['NewName']
    surname = request.POST['NewSurname']
    phonenumber= request.POST['NewNumber']
    phonebook.contacts_set.create(name_text=name, surname_text=surname, phonenumber_number=phonenumber)
    response = "Contact %s created"
    return HttpResponse(response % phonebook)


class PhonebookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = Phonebook.objects.all()
    serializer_class = PhonebookSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [permissions.IsAuthenticated]




