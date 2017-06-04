from django.db import models

from django.utils import timezone

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Category(models.Model):
	user = models.ForeignKey('auth.user')
	title = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class Post(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	body = models.TextField()
	image = models.FileField(upload_to='media/', default='media/default.png', max_length=100)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title

@receiver(pre_delete, sender=Post)
def mymodel_delete(sender, instance, **kwargs):
	if instance.image == "media/default.png":
		pass
	else:
		instance.image.delete(False)
