from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response

from .models import Gap
from .forms import GapForm


################################################################################
class GapList(generic.ListView):
    model = Gap


################################################################################
class GapDetail(generic.DetailView):
    model = Gap


################################################################################
class GapUpdate(UpdateView):
    model = Gap
    success_url = reverse_lazy('listGap')


################################################################################
class GapDelete(DeleteView):
    model = Gap
    success_url = reverse_lazy('listGap')


################################################################################
class GapNew(CreateView):
    model = Gap
    form_class = GapForm

    def get_success_url(self):
        return reverse_lazy('detailGap', kwargs={'pk': self.object.id})


################################################################################
def gapIndex(request):
    return render_to_response('gap/gap_index.html', {})

# EOF
