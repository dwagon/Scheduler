# forms.py
from django import forms
from .models import Gap


class GapForm(forms.ModelForm):
    desc = forms.CharField()
    start = forms.DateField()
    end = forms.DateField()

    class Meta:
        model = Gap

# EOF
