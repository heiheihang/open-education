from django.shortcuts import get_object_or_404,render

# Create your views here.
from django.http import HttpResponse
from .models import Student

def index(request):
	top_students = Student.objects.order_by('-point')[:3]
	context = {'student_list': top_students}
	return render(request, 'mllearning/index.html', context)

def student_detail(request, student_id):
	student = get_object_or_404(Student,pk=student_id)
	return render(request, 'mllearning/student.html', {'student' : student})

def class_detail(request, class_id):
	return HttpResponse("You are looking at class %s." % class_id)