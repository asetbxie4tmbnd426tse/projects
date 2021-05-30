#from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm

# Create your views here.

#def log_in(request):
#    pass

def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/register/successfullSignUp/")
    else:
        form = RegistrationForm()
    context = {"form":form}
    return render(request,"registration/sign-up.html", context)

def successfull_sign_up(request):
    context = {}
    return render(request,"registration/successfull-sign-up.html", context)

def successfull_logout(request):
    context = {}
    return render(request,"registration/successfull-logout.html", context)