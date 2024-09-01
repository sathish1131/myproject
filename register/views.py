from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if User.objects.filter(username=username) or User.objects.filter(email=email):
            messages.info(request, 'User Name or Email already exists!!!')
            return redirect('register')
        elif password != confirm_password:
            messages.info(request, 'Password is not matching!!!')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            user.save()
            return redirect('login')
    else:
        return render(request, 'register.html')