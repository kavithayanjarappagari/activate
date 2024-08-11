
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,'index.html')
def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method=="POST":
        usern=request.POST.get('uname')
        pasword=request.POST.get('passw')
        print(usern,pasword)
        result=authenticate(request,username=usern,password=pasword) 
        if result is not None:
            login(request,result)
            if request.user.is_superuser:
                 
                return redirect('/admin') 
            else:
                return redirect('loginpage') 
    return render(request,'login.html')

@login_required(login_url='loginpage')
def profile(request):
    return render(request,'profile.html')
def register(request):
    if request.method=="POST":
        usern=request.POST.get('uname')
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        email=request.POST.get('mail')
        pas=request.POST.get('passw')
        confirmpass=request.POST.get('cpass')
        print(usern,firstname,lastname,email,pas,confirmpass)
        if User.objects.filter(username=usern).exists():
            return redirect('registerpage')
        if len(pas)==8:
             return redirect('registerpage')
        if (confirmpass!=pas):
             return redirect('registerpage')
        obj=User.objects.create_user(username=usern,first_name=firstname,last_name=lastname,email=email) 
        obj.save() 
        return redirect('loginpage')  

    return render(request,'register.html')
def display(request):
    return render(request,'display.html')
@login_required(login_url='loginpage')
def tweet_view(request):
    if request.method=="POST":
        postn=request.POST.get('pname')
        obj=tweet_view(username=request.user.username,post=postn)
        obj.save()
        print(postn)
        return redirect('homepage')

    return render(request,'display.html')
def logoutV(request):
    logout(request)
    return redirect('loginpage')

def create(request):
    return render(request,'create.html')