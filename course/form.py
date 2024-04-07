from django import forms
from .models import * 

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

class UpdateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

class AddModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['content', 'title']

class UpdateModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['course', 'content', 'title']