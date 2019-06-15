from django.contrib import admin

from client_crud.models import Client, Address

admin.site.register(Client)
admin.site.register(Address)
