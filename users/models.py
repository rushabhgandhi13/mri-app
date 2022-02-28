from django.db import models
from django.contrib.auth.models import User
# Create your models here.
user_choices = (
	("Doctor", "Doctor"),
	("Patient", "Patient"),
	("Lab_user", "Lab_user"),
	
)
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	category = models.CharField(max_length = 20,choices=user_choices,default='Patient',blank=True, null=True)
	user_details = models.CharField(max_length=500,default='details')

	def __str__(self):
		return f'{self.user.username} Profile '