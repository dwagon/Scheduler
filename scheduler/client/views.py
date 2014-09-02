import datetime
import calendar

from django.shortcuts import render_to_response, redirect
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from .models import Client
from gap.models import inGap
from visit.models import Visit, makeVisits
from .forms import ClientForm

mnames = "January February March April May June July August September October November December".split()


################################################################################
class ClientList(generic.ListView):
    model = Client


################################################################################
class ClientDetail(generic.DetailView):
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
class ClientUpdate(UpdateView):
    model = Client
    success_url = reverse_lazy('listClients')


################################################################################
class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('listClients')


################################################################################
class ClientNew(CreateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse_lazy('detailClient', kwargs={'pk': self.object.id})


################################################################################
def visitDelete(requst, pk):
    """ Delete all the visits for a client """
    c = Client.objects.get(pk=pk)
    for v in Visit.objects.filter(client=c):
        v.delete()
    return redirect("detailClient", pk=pk)


################################################################################
def generateVisits(request, pk):
    c = Client.objects.get(pk=pk)
    if c.startdate:
        start = c.startdate
    else:
        start = datetime.date(2014, 1, 1)
    if c.enddate:
        end = c.enddate
    else:
        end = datetime.date(2015, 12, 31)
    msgs = makeVisits(c, start, end)
    for msg in msgs:
        messages.info(request, msg)
    return redirect("detailClient", pk=pk)


################################################################################
def displayDay(request, year=None, month=None, day=None):
    return redirect("displayThisMonth")


################################################################################
def displayClientMonth(request, client, year=None, month=None):
    return displayMonth(request, year=year, month=month, client=client, template='client/month.html')


################################################################################
def monthDetail(year=None, month=None, change=None, client=None):
    today = datetime.date.today()
    if year is None:
        year = today.year
    else:
        year = int(year)
    if month is None:
        month = today.month
    else:
        month = int(month)

    # apply next / previous change
    if change in ("next", "prev"):
        now, mdelta = datetime.date(year, month, 15), datetime.timedelta(days=31)
        if change == "next":
            mod = mdelta
        elif change == "prev":
            mod = -mdelta
        year, month = (now+mod).timetuple()[:2]

    cal = calendar.Calendar()
    lst = [[]]
    week = 0

    # make month lists containing list of days for each week
    # each day tuple will contain list of visits and 'current' indicator
    for day in cal.itermonthdays(year, month):
        current = False
        visits = None
        gap = None
        dt = None
        if day:
            dt = datetime.date(year, month, day)
            if dt == today:
                current = True
            gap = inGap(dt)
            visits = Visit.objects.filter(date=dt)
            if client:
                visits = visits.filter(client=client)

        lst[week].append((day, visits, current, gap, dt))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1
    return {'year': year, 'month': month, 'month_days': lst, 'mname': mnames[month-1]}


################################################################################
def displayMonth(request, year=None, month=None, change=None, client=None, template='client/display_month.html'):
    """Listing of days in `month`."""
    d = monthDetail(year, month, change, client)
    return render_to_response(template, d)

# EOF
