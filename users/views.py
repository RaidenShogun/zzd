from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Profile


# Create your views here.
def userListView(request):
	return render(request, 'users/user_list.html', {
		'users': User.objects.all(), 
	})
