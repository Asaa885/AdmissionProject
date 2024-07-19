from django.urls import path
from app import views

urlpatterns = [
    path('api/student/', views.student, name='student'),
    
    
    
]    