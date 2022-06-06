from django.db import models


class Phonebook(models.Model):
    name_text = models.CharField(max_length=100, null=True)

class Contacts(models.Model):
    contacts = models.ForeignKey(Phonebook,on_delete=models.CASCADE)
    name_text = models.CharField(max_length=100, null=True)
    surname_text = models.CharField(max_length=100, null=True)
    phonenumber_number = models.CharField(max_length=100, null=True)

