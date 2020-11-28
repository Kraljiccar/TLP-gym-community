from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

# Create your views here.


def index(request):
    """ A view to return index page """

    return render(request, 'home/index.html')


class AboutView(TemplateView):
    template_name = "home/about.html"


class LoseweightView(TemplateView):
    template_name = "home/lose-weight.html"


class GainweightView(TemplateView):
    template_name = "home/gain-weight.html"


class EnduranceView(TemplateView):
    template_name = "home/endurance.html"


class LivehealthyView(TemplateView):
    template_name = "home/live-healthy.html"
