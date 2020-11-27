from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

# Create your views here.


def index(request):
    """ A view to return index page """

    return render(request, 'home/index.html')


class AboutView(TemplateView):
    template_name = "home/about.html"
