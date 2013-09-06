import sys
import datetime
import calendar

from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy

from .models import Visit
from client.models import Client

mnames = "January February March April May June July August September October November December".split()

################################################################################
class VisitList(generic.ListView):
    model = Visit

################################################################################
class VisitDetail(generic.DetailView):
    model = Visit

    def get_context_data(self, **kwargs):
        context = super(Visit, self).get_context_data(**kwargs)
        sys.stderr.write("kwargs=%s\n" % kwargs)
        #context['visits'] = Visit.objects.filter(client=)
        return context

################################################################################
class VisitUpdate(UpdateView):
    model = Visit
    success_url = reverse_lazy('listVisits')

################################################################################
class VisitDelete(DeleteView):
    model = Visit
    success_url = reverse_lazy('listVisits')

################################################################################
class VisitNew(CreateView):
    model = Visit
    success_url = reverse_lazy('listVisits')

################################################################################
def clearAllVisits(request):
    from .models import clearVisits
    clearVisits()
    return redirect("displayThisMonth")

################################################################################
def generateAllVisits(request):
    # Make this a form to get the start and end days
    from .models import makeVisits
    start=datetime.date(2013,1,1)
    end=datetime.date(2014,12,31)
    for c in Client.objects.all():
        makeVisits(c,start,end)
    return render(request, "client/index.html", {})

################################################################################
def displayDay(request, year=None, month=None, day=None):
    pass

################################################################################
def clearAllVisits(request):
    from .models import clearVisits
    clearVisits()
    return redirect("displayThisMonth")

#EOF
