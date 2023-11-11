from django.shortcuts import render, get_object_or_404

from .models import FieldModel


# Create your views here.

def instructors(request):
    return render(request, 'instructors.html')

def maps(request):
    return render(request, 'maps.html')

def fields(request):
    fields = FieldModel.objects.all()
    context = {
        'fields': fields
    }
    return render(request, 'fields.html', context)

def show_courses(request, field_id):
    field = get_object_or_404(FieldModel, id=field_id)
    courses = field.coursemodel_set.all()  # Retrieve all courses associated with the field
    context = {
        'field': field,
        'courses': courses,
    }
    return render(request, 'show_courses.html', context)


def contact(request):
    return render(request, 'contact.html')

def landing(request):
    return render(request, 'landing.html')
    

# class CourseViewSet(viewsets.ModelViewSet): 
#     # define queryset 
#     queryset = CourseModel.objects.all() 
      
#     # specify serializer to be used 
#     serializer_class = CourseSerializer 