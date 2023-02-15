from django.shortcuts import render
from helloapp.forms import con_form

# Create your views here.
def base(request):
    return render(request,"base.html")
def index(request):
    return render(request,"index.html")
def chirag(request):
    return render(request,"chirag.html")
def contact(request):
    form=con_form()
    
    if request.method=="POST":
        form=con_form(request.POST)
        if form.is_valid():
            form.save()
        
    return render(request,'contact.html',{'form':form})