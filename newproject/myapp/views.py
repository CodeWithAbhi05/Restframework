from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .
class employeesList(APIView):
    def get(self,request):
        employees1=employees.objects.all()
        serializer=employeesSerializer(employees1,many=True)
        return Response(serializer.data)
    def post(self):
        pass

# Create your views here.
