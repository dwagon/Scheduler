from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.core.urlresolvers import reverse_lazy

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
    success_url = reverse_lazy('listGaps')


################################################################################
class GapDelete(DeleteView):
    model = Gap
    success_url = reverse_lazy('listGaps')


################################################################################
class GapNew(CreateView):
    model = Gap
    form_class = GapForm

    def get_success_url(self):
        return reverse_lazy('detailGap', kwargs={'pk': self.object.id})


################################################################################
def index(request):
    template_name = "client/index.html"
    context = {}
    return render(request, template_name, context)


# EOF
