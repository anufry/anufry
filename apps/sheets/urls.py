from django.urls import path, re_path
from django.conf.urls import url
from .views import *

urlpatterns = [
	path('<slug:slug>/', sheet_detail, name='sheet_detail'),
]