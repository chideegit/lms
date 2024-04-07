from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Course(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    title = models.CharField(max_length=100)

class EnrolCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    
class CompletedModule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices = (
            ('Started', 'Started'), 
            ('Not Started', 'Not Started'), 
            ('Completed', 'Completed')
        ), 
        default = 'Not Started'
    )