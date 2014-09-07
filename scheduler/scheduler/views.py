import csv
from django.shortcuts import render
from django.http import HttpResponse

from client.models import Client
from visit.models import Visit


################################################################################
def index(request):
    template_name = "base/index.html"
    context = {}
    return render(request, template_name, context)


################################################################################
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

# EOF
