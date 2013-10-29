# forms.py
from django import forms
from .models import Visit

class VisitForm(forms.ModelForm):

    class Meta:
        model = Visit
        exclude = ('client', 'good')

#EOF
