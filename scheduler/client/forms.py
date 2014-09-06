# forms.py
from django import forms

from .models import Client, DOW_CHOICES, DUR_CHOICES


class ClientForm(forms.ModelForm):
    dayofweek = forms.ChoiceField(choices=DOW_CHOICES)
    duration = forms.ChoiceField(choices=DUR_CHOICES)
    regularity = forms.IntegerField()
    flexible = forms.BooleanField(required=False)
    startdate = forms.DateField(required=False)
    enddate = forms.DateField(required=False)
    note = forms.CharField(required=False, max_length=250)

    class Meta:
        model = Client

# EOF
