# forms.py
from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    flexible = forms.BooleanField(required=False)
    startdate = forms.DateField(required=False)
    enddate = forms.DateField(required=False)

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'note': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

# EOF
