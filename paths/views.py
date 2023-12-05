from django.shortcuts import render, get_object_or_404, redirect
from .models import FieldModel, CourseModel, FeedbackModel
from .forms import FeedbackForm

# Create your views here.

def show_feedback(request, course_id):
    course = get_object_or_404(CourseModel, id=course_id)
    feedbacks = FeedbackModel.objects.filter(course=course)
    
    context = {
        'course': course,
        'feedbacks': feedbacks,
    }
    return render(request, 'feedback.html', context)

def show_courses(request, field_id):
    field = get_object_or_404(FieldModel, id=field_id)
    courses = field.coursemodel_set.all()  # Retrieve all courses associated with the field
    context = {
        'field': field,
        'courses': courses,
    }
    return render(request, 'show_courses.html', context)

    
def fields(request):
    fields = FieldModel.objects.all()
    context = {
        'fields': fields
    }
    return render(request, 'fields.html', context)

def field_created(request):
    return render(request, 'field_created.html')

def instructors(request):
    return render(request, 'instructors.html')

def maps(request):
    return render(request, 'maps.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def contact(request):
    return render(request, 'contact.html')

def landing(request):
    fields = FieldModel.objects.all()
    context = {
        'fields': fields
    }
    return render(request, 'landing.html', context)

def submit_feedback(request, course_id):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.course_id = course_id
            feedback.save()
            return redirect('paths:feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'submit_feedback.html', {'form': form})

def feedback_success(request):
    return render(request, 'feedback_success.html')
    

def submit_feedback(request, course_id):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.course_id = course_id
            feedback.save()
            return redirect('paths:show_feedback', course_id=course_id)
    else:
        form = FeedbackForm()
    return render(request, 'submit_feedback.html', {'form': form})

