from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout as django_logout 
from .models import User
from django.contrib.auth.models import User as AuthUser
from  authentication.models import UserInfo





def home(request):
    return render(request,"main/home.html")





def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            existing_user = User.objects.get(username=username)
            messages.error(request, "Username already taken.")
            return redirect("register")
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, email=email, password=password)
            userinfo = UserInfo.objects.create(user=user, email=email)

            user = authenticate(request, username=username, password=password)
            auth_login(request, user)

            messages.success(request, "Registration successful. You are now logged in.")
            return redirect("success")
    
    return render(request, "main/register.html")



def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('home')
    else:
        messages.error(request, "Invalid email or password.")

    return render(request, 'main/login.html')




def custom_logout(request):
    django_logout(request)
    return redirect('home')



def success(request):
    return render(request,'main/success.html')