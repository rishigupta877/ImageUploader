from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"index.html")


def signup(request):

    if request.method=="POST":
        username=request.POST['username'];
        fname=request.POST['fname'];
        lname=request.POST['lname'];
        email=request.POST['email'];
        pass1= request.POST['pass1'];
        pass2=request.POST['pass2'];
    return render(request,"signup.html")
     
def signin(request):
    return render(request,"signin.html")
     
def signout(request):
    pass
     
     