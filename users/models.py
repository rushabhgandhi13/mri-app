from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
user_choices = (
	("Doctor", "Doctor"),
	("Patient", "Patient"),
	("Lab_user", "Lab_user"),
	
)
gender_choices = (
	("Male", "Male"),
	("Female", "Female"),
	
)
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	category = models.CharField(max_length = 20,choices=user_choices,default='Patient',blank=True, null=True)
	user_details = models.CharField(max_length=500,default='details')
	license_number = models.CharField(max_length=500,default="0000")
	degree= models.CharField(max_length=500,default='MBBS')
	age = models.IntegerField(default=18)
	gender=models.CharField(max_length = 20,choices=gender_choices,default='Male',blank=True, null=True)
	disease = models.CharField(max_length=500,default="None")
	labname = models.CharField(max_length=500,default="None")
	labaddress= models.CharField(max_length=500,default="None")
	def __str__(self):
		return f'{self.user.username} '
