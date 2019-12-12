from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# User Registration form that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	# Specifies the Model that the Form interacts with
	# Creates a new "User"
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']