# forms.py
from django import forms
from .models import Visit


class VisitForm(forms.ModelForm):

    class Meta:
        model = Visit
        widgets = {
            'note': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super(VisitForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': 'datepicker'})


class VisitNewForm(forms.ModelForm):

    class Meta:
        model = Visit
        exclude = ('attn',)
        widgets = {
            'note': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super(VisitNewForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': 'datepicker'})
        self.fields['client'].value = kwargs['initial']['client']

# EOF
