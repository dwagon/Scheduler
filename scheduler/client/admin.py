from django.contrib import admin
from client.models import Client, Gap, Visit, Notes

admin.site.register(Client)
admin.site.register(Gap)
admin.site.register(Visit)
admin.site.register(Notes)
