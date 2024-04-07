from django.urls import path 
from .views import * 

urlpatterns = [
    path('register-student/', register_student, name='register-student'), 
    path('register-educator/', register_educator, name='register-educator'), 
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout')
]