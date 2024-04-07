from django.urls import path 
from .views import * 

urlpatterns = [
    path('add-course/', add_course, name='add-course'), 
    path('update-course/<int:pk>/', update_course, name='update-course'), 
    path('delete-course/<int:pk>/', delete_course, name='delete-course'), 
    path('all-courses-educator/', all_courses_educator, name='all-courses-educator'),
    path('available-courses/', available_courses, name='available-courses'),
    path('enrol-course/<int:pk>/', enrol_course, name='enrol-course'),
    path('course-details/<int:pk>/', course_details, name='course-details'),
    path('student-enrolled-courses/', student_enrolled_courses, name='student-enrolled-courses'),
    path('course-details/<int:pk>/', course_details, name='course-details'),
    path('course-details/<int:pk>/', course_details, name='course-details'), 
    path('students-per-course/<int:pk>/', students_per_course, name='students-per-course'), 
    # save course

    path('add-module/<int:pk>/', add_module, name='add-module'), 
    path('update-module/<int:pk>/', update_module, name='update-module'), 
    path('modules-per-course/<int:pk>/', modules_per_course, name='modules-per-course'),
    path('delete-module/<int:pk>/', delete_module, name='delete-module'), 
    path('module-details/<int:pk>/', module_details, name='module-details'), 
    path('mark-as-completed/<int:pk>/', mark_as_completed, name='mark-as-completed')

]