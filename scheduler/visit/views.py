import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from .models import Visit
from .forms import VisitForm
from scheduler.views import LoginRequiredMixin
from client.models import Client

mnames = "January February March April May June July August September October November December".split()


################################################################################
class VisitList(LoginRequiredMixin, generic.ListView):
    model = Visit


################################################################################
class VisitDetail(LoginRequiredMixin, generic.DetailView):
    model = Visit

    def get_context_data(self, *args, **kwargs):
        context = super(VisitDetail, self).get_context_data(*args, **kwargs)
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
    model = Visit
    success_url = reverse_lazy('visitDetail')


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
    from .models import makeVisits
    start = datetime.date(2014, 1, 1)
    end = datetime.date(2015, 12, 31)
    for c in Client.objects.all().order_by('-duration'):
        msgs = makeVisits(c, start, end)
        for msg in msgs:
            messages.info(request, msg)
    return render(request, "base/index.html", {})


################################################################################
@login_required
def displayDay(request, year=None, month=None, day=None):
    pass

# EOF
