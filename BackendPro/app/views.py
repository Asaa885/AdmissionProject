from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def student(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(Student, many=True)
        return Response(serializer.data)
