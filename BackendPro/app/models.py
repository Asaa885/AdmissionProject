from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Course(models.Model):
    cName = models.CharField(max_length=50)
    courseCode = models.CharField(max_length=50)
    
    def __str__(self):
        return self.cName
    
    
class Teacher(models.Model):
    tName = models.CharField(max_length=100)
    t_Id = models.CharField(max_length=100)
    email = models.EmailField()
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tName
    
    
class Exam(models.Model):
    exName =models.CharField(max_length=100)
    duration =models.DurationField()
    time = models.TimeField()
    questionType = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.exName    
    
    
class Student(models.Model):
    stName = models.CharField(max_length=100)
    st_Id = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.stName
    
class Result(models.Model):
    grade = models.CharField(max_length=5)
    marks = models.DecimalField(max_digits=5, decimal_places=2) 
    gpa = models.DecimalField(max_digits=1, decimal_places=1 )
    course =models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.grade   
        
    
