from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from client_crud.forms import ClientForm, AddressForm
from django.views import View

from client_crud.models import Client


def get_clients_by_filter(filter_type, filter):
    clients = list()
    if filter_type == 'All Clients':
        clients = list(Client.objects.all())
    elif filter_type == 'Name':
        clients = list(Client.objects.filter(name=filter))
    elif filter_type == 'Email':
        clients = list(Client.objects.filter(email=filter))
    elif filter_type == 'Phone':
        clients = list(Client.objects.filter(phone=filter))
    elif filter_type == 'Suburb':
        clients = list(Client.objects.filter(address__suburb=filter))
    return clients


def sort_clients_by_attr(order_type, clients):
    if order_type == 'Name':
        clients = sorted(clients, key=lambda x: x.name)
    elif order_type == 'Email':
        clients = sorted(clients, key=lambda x: x.email)
    elif order_type == 'Phone':
        clients = sorted(clients, key=lambda x: x.phone)
    elif order_type == 'Suburb':
        clients = sorted(clients, key=lambda x: x.address.suburb)
    return clients


class ClientList(View):
    def get(self, request):
        clients = list(Client.objects.all())
        return render(request, 'client_crud/list.html', {'clients': clients})

    def post(self, request):
        filter = request.POST.get('filter')
        filter_type = request.POST.get('filter_type')
        order_type = request.POST.get('order_type')
        clients = get_clients_by_filter(filter_type, filter)
        sorted_clients = sort_clients_by_attr(order_type, clients)
        return render(request, 'client_crud/list.html', {'clients': sorted_clients})


class CreateView(View):
    def get(self, request):
        client_form = ClientForm()
        address_form = AddressForm()
        return render(request, 'client_crud/create.html',
                      {'client_form': client_form, 'address_form': address_form})

    def post(self, request):
        client_form = ClientForm(request.POST)
        address_form = AddressForm(request.POST)
        if client_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            client = client_form.save(commit=False)
            client.address = address
            client.save()
            return HttpResponse('Client Created')
        else:
            return HttpResponse('Invalid ' + str(client_form.errors))


class UpdateView(View):
    def get(self, request, id):
        client = get_object_or_404(Client, id=id)
        client_form = ClientForm(instance=client)
        address_form = AddressForm(instance=client.address)
        return render(request, 'client_crud/create.html',
                      {'client_form': client_form, 'address_form': address_form, })

    def post(self, request, id):
        client_form = ClientForm(request.POST)
        address_form = AddressForm(request.POST)
        if client_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            client = get_object_or_404(Client, id=id)
            client.name = client_form.data['name']
            client.email = client_form.data['email']
            client.phone = client_form.data['phone']
            client.address = address
            client.save()
            return HttpResponse('Client Updated')
        else:
            return HttpResponse('Invalid ' + str(client_form.errors))
