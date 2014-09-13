# forms.py
from django import forms
from .models import Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        exclude = ('client',)
        widgets = {
            'note': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

# EOF
