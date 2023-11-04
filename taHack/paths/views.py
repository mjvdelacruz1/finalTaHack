from django.shortcuts import render

from .models import CourseModel


# Create your views here.

def login(request):
    return render(request, 'login.html')

def courses(request):
    return render(request,'courses.html')

def roadmap(request):
    return render(request, 'roadmap.html')

def landing(request):
    return render(request, 'landing.html')

# class CourseViewSet(viewsets.ModelViewSet): 
#     # define queryset 
#     queryset = CourseModel.objects.all() 
      
#     # specify serializer to be used 
#     serializer_class = CourseSerializer 