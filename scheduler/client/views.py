from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy

from .models import Client
from .forms import ClientForm

class ClientList(generic.ListView):
    model = Client

class ClientDetail(generic.DetailView):
    model = Client

class ClientUpdate(UpdateView):
    model = Client
    success_url = reverse_lazy('listClients')

class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('listClients')

class ClientNew(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('listClients')

def index(request):
    template_name = "client/index.html"
    context={}
    return render(request, template_name, context)

def viewCalendar(request):
    return render(request, "client/index.html", {})

def generateVisits(request):
    return render(request, "client/index.html", {})

#EOF
