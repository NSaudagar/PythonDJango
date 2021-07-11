from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, filters

# Create your views here.
from tickets.models import Ticket
from tickets.serializers import TicketSerializer


# def about(request):
#     return HttpResponse('This is Ticket Management System for AM/NS Employees')

class SearchTicketFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class ListTicketsView(generics.ListAPIView):
    filter_backends = (SearchTicketFilter,)
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class CreateTicketView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class UpdateTicketView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class DeleteTicketView(generics.DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


