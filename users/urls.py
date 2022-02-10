from django.urls import path
from . import views

urlpatterns = [
	path('', views.userListView, name="user-list"), 
]