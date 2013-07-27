# forms.py
from django import forms
from .models import Client, DOW_CHOICES, DUR_CHOICES

class ClientForm(forms.ModelForm):
    #name=forms.CharField()
    #regularity=forms.IntegerField()
    dayofweek=forms.ChoiceField(choices=DOW_CHOICES)
    duration=forms.ChoiceField(choices=DUR_CHOICES)
    ##note=forms.ForeignKey('Notes', null=True, blank=True)

    class Meta:
        model = Client

#EOF
