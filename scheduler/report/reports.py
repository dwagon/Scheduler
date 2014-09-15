import datetime
import calendar

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from gap.models import inGap
from visit.models import Visit
from client.models import Client

mnames = "January February March April May June July August September October November December".split()

allvisits = None


###############################################################################
@login_required
def reportIndex(request):
    return render(request, "report/index.html", {})


################################################################################
def monthDetail(year=None, month=None, change=None):
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
        if day:
            dd = dayDetails(year, month, day)
            lst[week].append(dd)
        else:
            lst[week].append({'real': False})
        if len(lst[week]) == 7:
            lst.append([])
            week += 1
    return {'year': year, 'month': month, 'month_days': lst, 'mname': mnames[month-1]}


################################################################################
def dayDetails(year, month, day):
    dt = datetime.date(year, month, day)
    gap = inGap(dt)
    visits = Visit.objects.filter(date=dt)
    today = (dt == datetime.date.today())
    return {
        'date': dt,
        'gap': gap,
        'visits': visits,
        'today': today,
        'day': dt.day,
        'month': dt.month,
        'year': dt.year,
        'real': True
        }


################################################################################
@login_required
def displayMonth(request, year=None, month=None, change=None, template='report/display_month.html'):
    """Listing of days in `month`."""
    d = monthDetail(year, month, change)
    return render(request, template, d)


################################################################################
@login_required
def displayYear(request, year=None):
    today = datetime.date.today()
    if year is None:
        year = today.year
    else:
        year = int(year)
    d = {}
    for month in range(1, 13):
        d["m%s" % month] = monthDetail(year, month)
    return render(request, "report/display_year.html", d)


################################################################################
@login_required
def displayDay(request, year=None, month=None, day=None):
    # TODO
    pass


################################################################################
@login_required
def exportData(request):
    import csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="schedule.csv"'
    writer = csv.writer(response)
    writer.writerow(['Client', 'Visit', 'Notes'])

    for client in Client.objects.all():
        writer.writerow([client.name, None, client.note])
        for visit in Visit.objects.filter(client=client):
            writer.writerow(['', visit.date, visit.note])
    return response


################################################################################
@login_required
def clientReport(request):
    d = {}
    d['clients'] = Client.objects.all()
    return render(request, "report/customer_report.html", d)

# EOF
