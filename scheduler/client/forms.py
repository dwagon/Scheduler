# forms.py
from django import forms
from .models import Client, DOW_CHOICES, DUR_CHOICES


class ClientForm(forms.ModelForm):
    dayofweek = forms.ChoiceField(choices=DOW_CHOICES)
    duration = forms.ChoiceField(choices=DUR_CHOICES)

    class Meta:
        model = Client

# EOF
