from django.http import HttpResponse
from django.views import generic
from .models import Client

class IndexView(generic.ListView):
    model = Client

class DetailView(generic.DetailView):
    model = Client
