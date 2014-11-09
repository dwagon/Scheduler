from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from .models import Visit
from .forms import VisitForm, VisitNewForm
from scheduler.views import LoginRequiredMixin
from client.models import Client
from report.reports import monthDetail

import sys


################################################################################
class VisitList(LoginRequiredMixin, generic.ListView):
    model = Visit


################################################################################
class VisitDetail(LoginRequiredMixin, generic.DetailView):
    model = Visit

    def get_context_data(self, *args, **kwargs):
        context = super(VisitDetail, self).get_context_data(*args, **kwargs)
        visit = kwargs['object']
        d = monthDetail(year=visit.date.year, month=visit.date.month)
        context['year'] = visit.date.year
        context['month'] = visit.date.month
        context['month_days'] = d['month_days']
        context['mname'] = d['mname']
        return context

    def get_success_url(self):
        return reverse_lazy('clientDetail', kwargs={'pk': self.object.client.id})


################################################################################
class VisitUpdate(LoginRequiredMixin, UpdateView):
    model = Visit
    form_class = VisitForm

    def get_success_url(self):
        return reverse_lazy('visitDetail', kwargs={'pk': self.object.id})


################################################################################
class VisitDelete(LoginRequiredMixin, DeleteView):
    model = Visit

    def get_success_url(self):
        return reverse_lazy('clientDetail', kwargs={'pk': self.object.client.id})


################################################################################
class VisitNew(LoginRequiredMixin, CreateView):
    fields = ['date', 'note']
    model = Visit
    form_class = VisitNewForm

    def get_success_url(self):
        return reverse_lazy('clientDetail', kwargs={'pk': self.kwargs.get('clientid')})

    def get_form_kwargs(self):
        kwargs = super(VisitNew, self).get_form_kwargs()
        kwargs['initial']['client'] = Client.objects.get(id=self.kwargs.get('clientid'))
        sys.stderr.write("kwargs=%s\n" % kwargs)
        return kwargs

    def get_initial(self, *args, **kwargs):
        initial = super(VisitNew, self).get_initial()
        initial['client'] = Client.objects.get(id=self.kwargs.get('clientid'))
        sys.stderr.write("initial=%s\n" % initial)
        return initial


################################################################################
@login_required
def clearAllVisits(request):
    from .models import clearVisits
    clearVisits()
    return redirect("index")


################################################################################
@login_required
def generateAllVisits(request):
    # Make this a form to get the start and end days
    for c in Client.objects.all().order_by('-duration'):
        msgs = c.makeVisits()
        for msg in msgs:
            messages.info(request, msg)
    return render(request, "base/index.html", {})

# EOF
