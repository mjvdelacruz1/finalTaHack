from django.shortcuts import render, get_object_or_404

from .models import FieldModel
from .forms import FieldForm


# Create your views here.

def field_create(request):
    context = {}
    form = FieldForm
    context['title'] = 'Make a Field'
    if request.method == 'POST':
        if 'save' in request.POST:
            form = FieldForm(request.POST)
            form.save()
    context['form'] = form
    return render(request, 'field_create.html', context)

def field_created(request):
    return render(request, 'field_created.html')

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

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def contact(request):
    return render(request, 'contact.html')

def landing(request):
    return render(request, 'landing.html')
    
# class CourseViewSet(viewsets.ModelViewSet): 
#     # define queryset 
#     queryset = CourseModel.objects.all() 
      
#     # specify serializer to be used 
#     serializer_class = CourseSerializer 