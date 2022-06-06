from django.contrib import admin

from .models import Phonebook, Contacts
# Register your models here.

admin.site.register(Phonebook)
admin.site.register(Contacts)
