from django.urls import path

from .views import *

urlpatterns = [
	path('', PostList.as_view(), name='blog_list'),
	path('<slug:slug>/', PostItem.as_view(), name='blog_item'),
]