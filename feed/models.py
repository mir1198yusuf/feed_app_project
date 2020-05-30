from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create your models here.

class Post(models.Model):
	message = models.CharField(max_length=5000)
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='posts', null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	file = models.FileField(blank=True)	#optional field

	def __str__(self):
		return self.message

class Comment(models.Model):
	message = models.CharField(max_length=2000)
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments', null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post, on_delete=models.SET_NULL, related_name='comments', null=True)

	def __str__(self):
		return self.message
	
class PostUser_Upvotes(models.Model):
	post = models.ForeignKey(Post, on_delete=models.SET_NULL, related_name='upvotes', null=True)
	upvoted_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='upvotes', null=True)

	def __str__(self):
		return self.post.message + '-' + self.upvoted_by.username

	
