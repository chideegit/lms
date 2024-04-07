from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .form import * 
from .models import * 
from django_project.decorator import only_educator, only_student

@login_required
@only_educator
def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.author = request.user
            var.save()
            messages.success(request, f'New course added - {var.title}')
            return redirect('all-courses-educator')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('add-course')
    else:
        form = AddCourseForm()
        context = {'form':form}
    return render(request, 'course/add_course.html', context)

@login_required
@only_educator
def update_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course information is now updated')
            return redirect(reverse('update-course', args=[course.pk]))
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            return redirect(reverse('update-course', args=[course.pk]))
    else:
        form = UpdateCourseForm(instance=course)
        context = {
            'form':form, 
            'course':course
        }
    return render(request, 'course/update_course.html', context)

@login_required
@only_educator
def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    messages.success(request, 'Course has been deleted')
    return redirect('all-courses-educator')

@login_required
@only_educator
def all_courses_educator(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request, 'course/all_courses_educator.html', context)

@login_required
@only_educator
def add_module(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddModuleForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.course = course
            var.save()
            messages.success(request, 'New module has been added to the course')
            return redirect(reverse('modules-per-course', args=[course.pk]))
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            return redirect(reverse('add-module', args=[course.pk]))
    else:
        form = AddModuleForm()
        context = {'form':form, 'course':course}
    return render(request, 'course/add_module.html', context)

@login_required
@only_educator
def update_module(request, pk):
    module = Module.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            messages.success(request, 'Module information is now updated and saved')
            return redirect(reverse('modules-per-course', args=[module.course.pk]))
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect(reverse('update-module', args=[module.pk]))
    else:
        form = UpdateModuleForm(instance=module)
        context = {'form':form, 'module':module}
    return render(request, 'course/update_module.html', context)

@login_required
@only_educator
def delete_module(request, pk):
    module = Module.objects.get(pk=pk)
    module.delete()
    messages.success(request, 'Module has been deleted from course')
    return redirect(reverse('modules-per-course', args=[module.course.pk]))

@login_required
@only_educator
def modules_per_course(request, pk):
    course = Course.objects.get(pk=pk)
    modules = course.module_set.all()
    context = {
        'course':course, 
        'modules':modules
    }
    return render(request, 'course/modules_per_course.html', context)

@login_required
@only_student
def available_courses(request):
    courses = Course.objects.filter(is_available=True)
    context = {'courses':courses}
    return render(request, 'course/available_courses.html', context)

@login_required
@only_student
def enrol_course(request, pk):
    course = Course.objects.get(pk=pk)
    if not EnrolCourse.objects.filter(course=course, student=request.user).exists():
        EnrolCourse.objects.create(
            course = course, 
            student = request.user
        )
        messages.success(request, 'You are now enrolled to this course. Enjoy the learing experience!')
        return redirect(reverse('course-details', args=[course.pk]))
    else:
        messages.warning(request, 'You are already enrolled for this course.')
        return redirect(reverse('course-details', args=[course.pk]))

@login_required
def course_details(request, pk):
    course = Course.objects.get(pk=pk)
    modules = course.module_set.all()

    if EnrolCourse.objects.filter(course=course, student=request.user).exists():
        has_enrolled = True
    else:
        has_enrolled = False

    context = {'course':course, 'modules':modules, 'has_enrolled':has_enrolled}
    return render(request, 'course/course_details.html', context)

@ login_required
@only_student
def student_enrolled_courses(request):
    courses = EnrolCourse.objects.filter(student=request.user)
    context = {'courses':courses}
    return render(request, 'course/student_enrolled_courses.html', context)

@login_required
@only_educator
def students_per_course(request, pk):
    course = Course.objects.get(pk=pk)
    students = course.enrolcourse_set.all()
    context = {'course':course, 'students':students}
    return render(request, 'course/students_per_course.html', context)

@login_required
def module_details(request, pk):
    module = Module.objects.get(pk=pk)
    if CompletedModule.objects.filter(module=module, user=request.user).exists():
        is_complete = True
    else:
        is_complete = False
    context = {'module':module, 'is_complete':is_complete}
    return render(request, 'course/module_details.html', context)

@login_required
@only_student
def mark_as_completed(request, pk):
    module = Module.objects.get(pk=pk)
    if not CompletedModule.objects.filter(module=module, user=request.user).exists():
        CompletedModule.objects.create(
            module = module, 
            user = request.user, 
            status = 'Completed'
        )
        messages.success(request, 'Module marked as completed')
        return redirect(reverse('course-details', args=[module.course.pk]))
    else:
        messages.warning(request, 'Module is already marked as completed')
        return redirect(reverse('course-details', args=[module.course.pk]))

# saved courses - write this func and let me know if it worked well for you! Happy coding :)
