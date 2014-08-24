import datetime
import calendar

from django.shortcuts import render, render_to_response, redirect
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from .models import Client, Day, inGap
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
        context['visits'] = Visit.objects.filter(client=kwargs['object'])
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
        return reverse_lazy('detailClient', pk=self.object.id)


################################################################################
def index(request):
    template_name = "client/index.html"
    context = {}
    return render(request, template_name, context)


################################################################################
def generateVisits(request, pk):
    start = datetime.date(2014, 1, 1)
    end = datetime.date(2015, 12, 31)
    c = Client.objects.get(pk=pk)
    msgs = makeVisits(c, start, end)
    for msg in msgs:
        messages.info(request, msg)
    return redirect("detailClient", pk=pk)


################################################################################
def displayDay(request, year=None, month=None, day=None):
    return redirect("displayThisMonth")


################################################################################
def displayMonth(request, year=None, month=None, change=None):
    """Listing of days in `month`."""
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
        gap = False
        d = None
        if day:
            dt = datetime.date(year, month, day)
            if dt == today:
                current = True
            d = Day.objects.get_or_create(date=dt, defaults={'date': dt})[0]
            if inGap(dt):
                gap = True
            visits = Visit.objects.filter(date=d)

        lst[week].append((day, visits, current, gap, d))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1

    return render_to_response("client/month.html", dict(year=year, month=month, month_days=lst, mname=mnames[month-1]))

# EOF
