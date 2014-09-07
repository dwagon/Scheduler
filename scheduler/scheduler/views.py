from django.shortcuts import render


################################################################################
def index(request):
    template_name = "base/index.html"
    context = {}
    return render(request, template_name, context)

# EOF
