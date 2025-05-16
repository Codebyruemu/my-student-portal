from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate,login,logout
from . models import *

# Create your views here.
def indexPage(request):
    products=Good.objects.all()
    context={'products':products}
    return render(request, 'Items/index.html',context)


def registerPage(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        # This code below recieve the form posted form information as argument and also send thesame information to django User which is backend
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'An account was created for'+ user)
            return redirect('login')
    context = {'form':form}
        
    return render(request, 'Items/register.html', context)


def loginPage(request):
    if request.method =='POST':
        # post is a dictionary and when you pass in the get function to it return the value 
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            # the login function below id django login not same with the dynamic login we have in registration page
            login(request, user)
            return redirect('post')
        else:
            messages.info(request, 'username of password is INCORRECT')
    return render(request, 'Items/login.html')

def postPage(request):
    
    form = CreatePost()
    if request.method=='POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save()
            newpost.save()
            return redirect('home')
        else:
            form = form.CreatePost()
    return render(request, 'Items/post.html',{'form':form})

