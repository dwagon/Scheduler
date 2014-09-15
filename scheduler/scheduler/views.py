from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


################################################################################
@login_required
def index(request):
    template_name = "base/index.html"
    return render(request, template_name, context_instance=RequestContext(request))


################################################################################
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

# EOF
