from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
	
	# membuat relationship
	user = models.OneToOneField(User)
	#add any addtional 
	portfolio_site = models.URLField(blank=True)
	#pip install pillow dulu brow
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

	def __str__(self):
		return self.user.username
