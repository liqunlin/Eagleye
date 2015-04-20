from django.db import models

class Student(models.Model):
	name=models.CharField(max_length=50)
	age=models.IntegerField(max_length=10)

class Subject(models.Model):
	student=models.ForeignKey(Student)
	sub_name=models.CharField(max_length=20)
	sub_num=models.IntegerField(default=0)

