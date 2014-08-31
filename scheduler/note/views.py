from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy

from .models import Note
from .forms import NoteForm


################################################################################
class NoteList(generic.ListView):
    model = Note


################################################################################
class NoteDetail(generic.DetailView):
    model = Note


################################################################################
class NoteUpdate(UpdateView):
    model = Note
    success_url = reverse_lazy('listNote')


################################################################################
class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('listNote')


################################################################################
class NoteNew(CreateView):
    model = Note
    form_class = NoteForm

    def get_success_url(self):
        return reverse_lazy('detailNote', kwargs={'pk': self.object.id})

# EOF
