from django.shortcuts import render

from .models import CourseModel


# Create your views here.

def instructors(request):
    return render(request, 'instructors.html')

def maps(request):
    return render(request, 'maps.html')

def courses(request):
    courses = CourseModel.objects.all()
    context = {
        'courses': courses
    }
    return render(request,'courses.html', context)

def contact(request):
    return render(request, 'contact.html')

def landing(request):
    return render(request, 'landing.html')
    

# class CourseViewSet(viewsets.ModelViewSet): 
#     # define queryset 
#     queryset = CourseModel.objects.all() 
      
#     # specify serializer to be used 
#     serializer_class = CourseSerializer 