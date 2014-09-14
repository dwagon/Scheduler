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
            'note': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['regularity'].widget.attrs.update({'class': 'form-control'})
        self.fields['dayofweek'].widget.attrs.update({'class': 'form-control'})
        self.fields['duration'].widget.attrs.update({'class': 'form-control'})
        self.fields['flexible'].widget.attrs.update({'class': 'form-control'})
        self.fields['startdate'].widget.attrs.update({'class': 'form-control'})
        self.fields['enddate'].widget.attrs.update({'class': 'form-control', 'type': 'date'})

# EOF
