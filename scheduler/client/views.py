from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from .models import Client
from visit.models import Visit
from scheduler.views import LoginRequiredMixin
from .forms import ClientForm
from report.reports import monthDetail


################################################################################
class ClientList(LoginRequiredMixin, generic.ListView):
    model = Client


################################################################################
class ClientDetail(LoginRequiredMixin, generic.DetailView):
    model = Client

    def get_context_data(self, *args, **kwargs):
        context = super(ClientDetail, self).get_context_data(*args, **kwargs)
        client = kwargs['object']
        d = monthDetail(client=client)
        context['visits'] = Visit.objects.filter(client=client)
        context['year'] = d['year']
        context['month'] = d['month']
        context['month_days'] = d['month_days']
        context['mname'] = d['mname']
        context['client'] = client
        return context


################################################################################
class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse_lazy('clientDetail', kwargs={'pk': self.object.id})


################################################################################
class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clientList')


################################################################################
class ClientNew(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse_lazy('clientDetail', kwargs={'pk': self.object.id})


################################################################################
@login_required
def clientDeleteVisits(requst, pk):
    """ Delete all the visits for a client """
    c = Client.objects.get(pk=pk)
    for v in Visit.objects.filter(client=c):
        v.delete()
    return redirect("clientDetail", pk=pk)


################################################################################
@login_required
def clientGenerateVisits(request, pk):
    c = Client.objects.get(pk=pk)
    msgs = c.makeVisits()
    for msg in msgs:
        messages.info(request, msg)
    return redirect("clientDetail", pk=pk)


################################################################################
@login_required
def displayDay(request, year=None, month=None, day=None):
    return redirect("displayThisMonth")


################################################################################
@login_required
def clientIndex(request):
    return render(request, 'client/client_index.html')


################################################################################
@login_required
def deleteAllClients(request):
    for c in Client.objects.all():
        for v in Visit.objects.filter(client=c):
            v.delete()
        c.delete()
    return redirect("index")


# EOF
