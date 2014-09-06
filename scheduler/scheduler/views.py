from django.shortcuts import render, render_to_response


################################################################################
def index(request):
    template_name = "base/index.html"
    context = {}
    return render(request, template_name, context)


################################################################################
def miscIndex(request):
    return render_to_response('misc/misc_index.html', {})

# EOF
