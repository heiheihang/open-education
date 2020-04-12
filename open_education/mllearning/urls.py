from django.urls import path

from . import views
app_name = 'mllearning'

urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('class/<int:class_id>/', views.class_detail, name='class_detail'),
]
