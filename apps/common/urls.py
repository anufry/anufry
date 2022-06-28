from django.urls import path
from django.views.generic.base import RedirectView

from .views import HomePageView

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('favicon.ico', RedirectView.as_view(url='/static/core/images/favicon.ico', permanent=True)),
]