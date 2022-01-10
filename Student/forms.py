from django.core import validators
from django import forms
from .models import Student_Info, Student_Acadmics


class StudentRegistraion(forms.ModelForm):
	class Meta:
		model = Student_Info
		fields = ['Roll_no','Name','Class','School','Mobile','Address']
		widgets = {
		'Roll_no':forms.TextInput(attrs={'class':'form-control'}),
		'Name':forms.TextInput(attrs={'class':'form-control'}),
		'Class':forms.TextInput(attrs={'class':'form-control'}),
		'School':forms.TextInput(attrs={'class':'form-control'}),
		'Mobile':forms.TextInput(attrs={'class':'form-control'}),
		'Address':forms.TextInput(attrs={'class':'form-control'}),


		}


class StudentAcadmics(forms.ModelForm):
	class Meta:
		model = Student_Acadmics
		fields = ['Roll_no','Maths','Physics','Chemistry','Biology','English']
		widgets = {
		'Roll_no':forms.Select(attrs={'class':'form-control'}),
		'Maths':forms.TextInput(attrs={'class':'form-control'}),
		'Physics':forms.TextInput(attrs={'class':'form-control'}),
		'Chemistry':forms.TextInput(attrs={'class':'form-control'}),
		'Biology':forms.TextInput(attrs={'class':'form-control'}),
		'English':forms.TextInput(attrs={'class':'form-control'}),


		}
