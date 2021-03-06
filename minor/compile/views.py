from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, get_user_model,login,logout
from django.shortcuts import render, redirect


from .forms import UserLoginForm, UserRegisterForm
# Create your views here.


def testview(request):
	return HttpResponse("<h1> Done Deal</h1>")


def login_view(request):
	form = UserLoginForm(request.POST or None)
	title = "Login"
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		login(request,user)
		print(request.user.is_authenticated)
		return redirect("/")

	return render(request,"form.html",{'form':form,'title':title})

def register_view(request):
	title ="Register"
	form =UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit = False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username,password=password)
		login(request,new_user)
		return redirect("/")
	context = {"form":form, "title":title}
	return render(request,"form.html", context)

def logout_view(request):
	logout(request)
	return redirect("/")