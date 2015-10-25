from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import StudentForm
from .models import *
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def form(request):
	return render(request, 'form.html', {'form': StudentForm()})

def about(request):
	return render(request, 'about.html', {})

def submit(request):
	form = StudentForm(request.POST)
	form.is_valid()
	clean = form.cleaned_data
	entry = Student(university = clean['university'], first_name = clean['first_name'], last_name = clean['last_name'],
					email = clean['email'], department = clean['department'].upper(), course_number = clean['course_number'].upper(), 
					course_type = clean['course_type'].lower(), section = clean['section'], bio = clean['bio'])
	entry.save()
	return render(request, 'submit.html', {})

def search(request):
	return render(request, 'search.html', {'form': StudentForm()})

def result(request):
	form = StudentForm(request.POST)
	form.is_valid()
	clean = form.cleaned_data
	students = Student.objects.filter(university=clean['university']).filter(department=clean['department'].upper()).filter(course_number=clean['course_number'].upper())
	if 'course_type' in clean:
		students = students.filter(course_type=clean['course_type'].lower())
		if 'section' in clean:
			students = students.filter(section=clean['section'])
	return render(request, 'result.html', {'students': students})