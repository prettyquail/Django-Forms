from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from ModelForm.models import Register
from django.db.models.query import QuerySet


# Create your views here.

@login_required
def indexpage(request):
    return render(request,'ModelForm/index.html')

def registeruser(request):
	if request.user.is_authenticated:
		return redirect('indexpage')
	else:
		form = RegisterForm()
		if request.method == 'POST':
			form = RegisterForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('loginuser')
			

		context = {'form':form}
		return render(request, 'ModelForm/register.html', context)

def loginuser(request):
	if request.user.is_authenticated:
		return redirect('indexpage')
	else:

		if request.method == 'POST':
		    username = request.POST.get('username')
		    password = request.POST.get('password')
		    user = Register.objects.filter(username=username, password=password)
		    
		    if len(user):
		    	
		    	return render(request,'ModelForm/index.html',{'username': user[0].username})
		    else:
		        messages.error(request, "Invalid username or password.")
		context = {}
		return render(request, 'ModelForm/login.html', context)

def logoutuser(request):
	logout(request)
	return redirect('loginuser')



