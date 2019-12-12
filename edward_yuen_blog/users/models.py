from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Profile model, with 1-to-1 relationship to a User, CASCADE on delete
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'