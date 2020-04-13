from django.contrib import admin
from .models import Student, ClassGroup, Problem, Choice

admin.site.register(Student)
admin.site.register(ClassGroup)
admin.site.register(Problem)
admin.site.register(Choice)