from django.core.validators import RegexValidator
from django.db import models


class Address(models.Model):
    street_name = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=100, blank=True)


class Client(models.Model):
    phone_regex = RegexValidator(regex=r'^\+\d{2}\(?([0-9]{3})\)[0-9]{3}\-[0-9]{2}\-[0-9]{2}$',
                                 message="Phone must have the next format +38(068)111-11-11")
    name = models.CharField(max_length=100, unique=True)
    contact_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(validators=[phone_regex], max_length=17)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
