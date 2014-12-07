from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect

from .models import Gap
from .forms import GapForm
from scheduler.views import LoginRequiredMixin


################################################################################
class GapList(generic.ListView, LoginRequiredMixin):
    model = Gap


################################################################################
class GapDetail(LoginRequiredMixin, generic.DetailView):
    model = Gap


################################################################################
class GapUpdate(LoginRequiredMixin, UpdateView):
    model = Gap
    success_url = reverse_lazy('gapList')


################################################################################
class GapDelete(LoginRequiredMixin, DeleteView):
    model = Gap
    success_url = reverse_lazy('gapList')


################################################################################
class GapNew(LoginRequiredMixin, CreateView):
    model = Gap
    form_class = GapForm

    def get_success_url(self):
        return reverse_lazy('gapDetail', kwargs={'pk': self.object.id})


################################################################################
@login_required
def gapIndex(request):
    return render(request, 'gap/gap_index.html', {})


################################################################################
@login_required
def clearAllGaps(request):
    from .models import clearGaps
    clearGaps()
    return redirect("index")

# EOF
