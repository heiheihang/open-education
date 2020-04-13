from django.urls import path

from . import views
app_name = 'mllearning'

urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('class/<int:class_id>/', views.class_detail, name='class_detail'),
    path('problem/<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('problem/<int:problem_id>/vote/', views.vote, name='vote'),
    path('problem/<int:problem_id>/results/', views.results, name='results')
]
