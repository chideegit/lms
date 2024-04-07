from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .form import * 

def register_student(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_student = True
            var.username = var.email
            var.save()
            messages.success(request, 'Your student account is now created. Please log in')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('register-student')
    else:
        form = RegisterUserForm()
        context = {'form':form}
    return render(request, 'accounts/register_student.html', context)

def register_educator(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.username = var.email
            var.is_educator = True
            var.save()
            messages.success(request, 'Your educator account is now created. Please log in')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('register-educator')
    else:
        form = RegisterUserForm()
        context = {'form':form}
    return render(request, 'accounts/register_educator.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'Welcome! You are logged in as {user.first_name}')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Your active session is now ended. Log in to continue')
    return redirect('login')

# update profile
# change password in-app