from django.contrib import admin
from client.models import Client, Gap, Visit, Notes, Day

admin.site.register(Client)
admin.site.register(Gap)
admin.site.register(Visit)
admin.site.register(Notes)
admin.site.register(Day)
