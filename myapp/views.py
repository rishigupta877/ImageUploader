from django.shortcuts import redirect, render
from .forms import ImageForm
from .models import image 
# Create your views here.
def home(request):

    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
      
    form=ImageForm()
    img=image.objects.all()

    return render(request,"home.html",{'form':form,'img':img})