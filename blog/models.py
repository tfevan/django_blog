from django.db import models

from django.utils import timezone

class Category(models.Model):
	user = models.ForeignKey('auth.user')
	title = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class Post(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	body = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title