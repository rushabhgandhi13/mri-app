from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileRegisterForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['category']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_details']
        widgets = {
            'user_details' : forms.Textarea,
        
        }
        
class ProfileDoctor(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['age','gender','license_number','degree']
		
class ProfilePatient(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['age','gender','disease']
		
class ProfileLab(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['license_number','labname','labaddress']
		widgets = {
            'user_details' : forms.Textarea,
        
        }

