from django.urls import path
from client_crud import views

urlpatterns = [
    path('', views.ClientList.as_view(), name='clients_list'),
    path('create', views.CreateView.as_view(), name='client_create'),
    path('update/<int:id>', views.UpdateView.as_view(), name='client_update'),
]
