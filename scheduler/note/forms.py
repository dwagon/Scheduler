# forms.py
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    note = forms.CharField()

    class Meta:
        model = Note

# EOF
