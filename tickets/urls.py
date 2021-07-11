"""TicketMgmtSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from tickets import views

urlpatterns = [
    path('', views.ListTicketsView.as_view(), name="tickets-all"),
    path('create/', views.CreateTicketView.as_view(), name="tickets-create"),
    path('update/<int:pk>', views.UpdateTicketView.as_view(), name="tickets-update"),
    path('delete/<int:pk>', views.DeleteTicketView.as_view(), name="tickets-delete"),
]
