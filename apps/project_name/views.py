from django.shortcuts import render_to_response
from django.template.context import RequestContext


def home(request):
    template = 'home.html'
    context = {}
    return render_to_response(template,
                              RequestContext(request, context))
