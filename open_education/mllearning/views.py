from django.shortcuts import get_object_or_404,render
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student, ClassGroup, Problem, Choice

def index(request):
	top_students = Student.objects.order_by('-point')[:3]
	frequent_problem = Problem.objects.order_by('-problem_date')[:1]
	print(frequent_problem[0].problem_id)
	context = {'student_list': top_students, 'problem' : frequent_problem}

	return render(request, 'mllearning/index.html', context)

def student_detail(request, student_id):
	student = get_object_or_404(Student,pk=student_id)
	return render(request, 'mllearning/student.html', {'student' : student})

def problem_detail(request, problem_id):
	problem = get_object_or_404(Problem,pk=problem_id)
	return render(request, 'mllearning/problem.html', {'problem' : problem})

def class_detail(request, class_id):
	return HttpResponse("You are looking at class %s." % class_id)

def vote(request, problem_id):
	problem = get_object_or_404(Problem, pk=problem_id)
	try:
		selected_choice = problem.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'mllearning/problem.html', {
			'problem': problem,
		'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		return HttpResponseRedirect(reverse('mllearning:results', args=(problem.problem_id,)))	

def results(request, problem_id):
 	problem = get_object_or_404(Problem, pk=problem_id)
 	return render(request, 'mllearning/results.html', {'problem': problem})