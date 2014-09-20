# forms.py
from django import forms
from .models import Gap


class GapForm(forms.ModelForm):
    start = forms.DateField()
    end = forms.DateField()

    class Meta:
        model = Gap
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GapForm, self).__init__(*args, **kwargs)
        self.fields['start'].widget.attrs.update({'class': 'datepicker'})
        self.fields['end'].widget.attrs.update({'class': 'datepicker'})

# EOF
