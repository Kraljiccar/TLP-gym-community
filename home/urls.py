from django.urls import path
from . import views
from home.views import AboutView, LoseweightView, GainweightView

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('lose-weight/', LoseweightView.as_view(), name='lose-weight'),
    path('gain-weight/', GainweightView.as_view(), name='gain-weight'),
]
