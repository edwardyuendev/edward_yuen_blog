from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# User Registration form that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	# Specifies the Model that the Form interacts with
	# Creates a new "User"
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	# Form that will update our User Model
	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']