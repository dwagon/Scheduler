# forms.py
from django import forms
from .models import Gap


class GapForm(forms.ModelForm):
    class Meta:
        model = Gap
        fields = '__all__'

# EOF
