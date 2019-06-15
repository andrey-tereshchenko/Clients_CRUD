from django.forms import ModelForm
from django import forms

from client_crud.models import Client, Address


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'contact_name', 'email', 'phone']

        widgets = {'phone': forms.TextInput(attrs={'data-mask': "000-000-0000"})}


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street_name', 'suburb', 'postcode', 'state']
