from rest_framework import serializers

from .models import Phonebook, Contacts


class PhonebookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phonebook
        fields = ['id', 'name_text']
        depth = 1


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = ['id', 'name_text', 'surname_text', 'phonenumber_number']