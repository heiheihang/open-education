from django.db import models

# Create your models here.



class ClassGroup(models.Model):
	class_id = models.AutoField(primary_key=True)
	class_name = models.CharField(max_length=30, default = 'no name')
	year = models.IntegerField(default = 0)

class Student(models.Model):
	student_id = models.AutoField(primary_key=True)
	student_name = models.CharField(max_length=30)
	student_class = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
	point = models.IntegerField(default = 0)

class Problem(models.Model):
	problem_id = models.AutoField(primary_key=True)
	difficulty = models.IntegerField(default = 0)
	problem_text = models.CharField(max_length=300)
