from django.db import models

# Create your models here.
class Student_Info(models.Model):
	Roll_no = models.CharField(primary_key=True, max_length=1000)
	Name = models.CharField(max_length=100)
	Class = models.CharField(max_length=100)
	School = models.CharField(max_length=100)
	Mobile = models.CharField(max_length=10)
	Address = models.TextField()

	def __str__(self):
		return self.Name + '--' + self.Roll_no


class Student_Acadmics(models.Model):
	Roll_no = models.ForeignKey(Student_Info, on_delete=models.CASCADE)
	Maths = models.IntegerField()
	Chemistry = models.IntegerField()
	Physics = models.IntegerField()
	Biology = models.IntegerField()
	English = models.IntegerField()

	


