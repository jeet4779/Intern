from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "users/base.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Welcome {username}")
            return redirect("home")
    else:
        form=UserCreationForm()

   
    return render(request,"users/register.html",{'form':form})


def login(request):
    return HttpResponse("<h1>Hello</h1>")