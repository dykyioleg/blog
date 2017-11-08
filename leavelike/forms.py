from django import forms
from .models  import *
from django.contrib.auth.models import User


class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['entry_text']
		
		
		
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment_text']	


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password','email']


class UserAuthForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']