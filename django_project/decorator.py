from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import redirect

User = get_user_model()

def only_educator(view_func):
    def wrapper(request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        if not user.is_educator:
            messages.warning(request, 'Permission Denied. You are not allowed in there!')
            return redirect('dashboard')
        response = view_func(request, *args, **kwargs) 
        return response
    return wrapper

def only_student(view_func):
    def wrapper(request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        if not user.is_student:
            messages.warning(request, 'Permission Denied. You are not allowed in there!')
            return redirect('dashboard')
        response = view_func(request, *args, **kwargs) 
        return response
    return wrapper