from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Playlists(models.Model):
	name=models.CharField(max_length=50)
	description=models.TextField(max_length=250)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name}"
	
	def get_absolute_url(self):
		return reverse('detail', kwargs={'playlists_id': self.id})
	