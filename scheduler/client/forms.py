# forms.py
from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    startdate = forms.DateField(required=False)
    enddate = forms.DateField(required=False)

    def clean_duration(self):
        data = self.cleaned_data['duration']
        if data <= 0:
            raise forms.ValidationError("Visit duration must be greater than zero")
        if data >= 9:
            raise forms.ValidationError("Visit duration can't be greter than 8 hours")
        return data

    class Meta:
        model = Client
        fields = ['name', 'regularity', 'dayofweek', 'duration', 'note', 'startdate', 'enddate']
        widgets = {
            'note': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['regularity'].widget.attrs.update({'class': 'form-control'})
        self.fields['dayofweek'].widget.attrs.update({'class': 'form-control'})
        self.fields['duration'].widget.attrs.update({'class': 'form-control'})
        self.fields['startdate'].widget.attrs.update({'class': 'datepicker'})
        self.fields['enddate'].widget.attrs.update({'class': 'datepicker'})

# EOF
