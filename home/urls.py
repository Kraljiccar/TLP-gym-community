from django.urls import path
from . import views
from home.views import AboutView

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', AboutView.as_view(), name='about'),
]
