import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from client.models import Client
from visit.models import Visit


################################################################################
@login_required
def index(request):
    template_name = "base/index.html"
    return render(request, template_name, context_instance=RequestContext(request))


################################################################################
@login_required
def exportData(request):
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
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

# EOF
