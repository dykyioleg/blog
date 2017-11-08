from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entry(models.Model):
	user = models.ForeignKey(User,null=True)
	entry_text = models.TextField(verbose_name = 'text field',blank=True,null=True)
	pub_date = models.DateTimeField(auto_now_add = True)
	number_like = models.IntegerField(blank = True,default = 0)
	
	def short_text(self):
		return '{0}...'.format(self.entry_text[:150])
		
	def add_like(self):
		self.number_like += 1
		self.save()
		
	def __str__(self):
		return self.short_text()
	
class Comment(models.Model):
	user = models.ForeignKey(User,null=True)
	entry = models.ForeignKey(Entry)
	comment_text = models.TextField(verbose_name = 'comment')
	pub_date = models.DateTimeField(auto_now_add = True)
	
	def __str__(self):
		return self.comment_text