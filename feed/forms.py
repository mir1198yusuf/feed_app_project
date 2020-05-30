#this file contains all the custom built form classes
from django import forms
from feed.models import Post,Comment

class NewPost_Form(forms.ModelForm):
	class Meta:
		model = Post 
		fields = ['message', 'file']
		widgets = {'message':forms.Textarea()}

class NewComment_Form(forms.ModelForm):
	class Meta:
		model = Comment 
		fields = ['message']
		widgets = {'message': forms.Textarea()}