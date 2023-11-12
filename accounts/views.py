from django.shortcuts import render, redirect
from main.views import home
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser
# Create your views here.


def userlogin(request):
    

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)

        if user is not None :

            login(request, user)
            return redirect(home)
        else: 
   
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')

def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        
        print(username, email, phone_number, password)
        user = CustomUser.objects.create(username=username, email=email, phone_number=phone_number, password=password)
        user.save()
        return redirect(home)
    
    return render(request, 'sign-up.html')

    
