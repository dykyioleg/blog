from django.shortcuts import render,redirect
from .models import Entry,Comment
from django.urls import reverse
from .forms import EntryForm, CommentForm,UserForm,UserAuthForm
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout


# Create your views here.






class GetTextList(ListView):
	
	context_object_name = 'entrys'
	template_name = 'leavelike/entrys.html'
	
	def get_queryset(self):
		return Entry.objects.order_by('entry_text')
	

	
#def get_text(request):
#	context = Entry.objects.all()
#	dic_t = {'entrys':context}
#	return render(request,'leavelike/entrys.html',dic_t)

class GetObjectDetail(DetailView):
	model = Entry
	context_object_name = 'entry'
	template_name = 'leavelike/entry.html'
	
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		form = CommentForm()
		context['form'] = form
		return context
	
	
#def get_object(request,id):
#	form = CommentForm()
#	context = Entry.objects.get(id = id)
#	dic_t = {'entry':context,'form':form}
#	return render(request,'leavelike/entry.html',dic_t)
	
def likeup(request,id):
	object = Entry.objects.get(id = id)
	object.add_like()
	return redirect(reverse('simple-entry',args=[object.id]))
	
def addcomment(request,id):
	object = Entry.objects.get(id = id)
	if object.user == request.user:
		form = CommentForm(request.POST or None)
		if request.method == "POST" and form.is_valid():
			comment_text = form.cleaned_data['comment_text']
		com = object.comment_set.create(comment_text = comment_text)
		com.user = request.user
		com.save()
		return redirect(reverse('simple-entry',args=[object.id]))
	else:
		return redirect(reverse('auth-user'))
		
def delcomment(request,id):
	object_com = Comment.objects.get(id = id)
	object_ent = object_com.entry
	object_com.delete()
	return redirect(reverse('simple-entry',args=[object_ent.id]))
'''	
class UpdateEntry(UpdateView):
	form_class = EntryForm
	model = Entry
	template_name = 'leavelike/edit.html'
	
	def get_success_url(self):
		return reverse('simple-entry',args=[self.object.id])
'''

	
def editentry(request,id):
	object = Entry.objects.get(id = id)
	if object.user == request.user:
		form = EntryForm(request.POST or None)
		if request.method == "POST" and form.is_valid():
			data = form.cleaned_data
			object.entry_text = data["entry_text"]
			object.save()
			return redirect(reverse('simple-entry',args=[object.id]))
		else:
			form = EntryForm(initial={'entry_text':object.entry_text})
			context = {'entry':object,'form':form}
			return render(request,'leavelike/edit.html',context)
		
	else:

		return redirect(reverse('for-edit'))
	

def create_entry(request):
	if request.method == 'POST':
		form =  EntryForm(request.POST)
		if  form.is_valid():
			data = form.cleaned_data
			entry_text = data['entry_text']
			object = Entry(entry_text=entry_text)
			object.user = request.user
			object.save()
		
			return redirect(reverse('entrys'))

			
			
	else:
		form = EntryForm()
	return render(request,'leavelike/create_entry.html',{'form':form})


'''
class EntryCreate(CreateView):
	model = Entry
	fields = ['entry_text']
	template_name = 'leavelike/create_entry.html'
	
	def get_success_url(self):
		return reverse('simple-entry',args=[self.object.id])
'''
		

class EntryDelete(DeleteView):
	model = Entry
	success_url = reverse_lazy('entrys')
	context_object_name = 'entry'
	

def createform(request):
	if request.user.is_authenticated():
		return redirect(reverse('entrys'))
	if request.method == 'POST':
		form = UserForm(request.POST)
		if  form.is_valid():
			data = form.cleaned_data
			User.objects.create_user(username=data['username'],password=data['password'],email=data['email'])
			return redirect(reverse('entrys'))
	else:
		form = UserForm()
	return render(request,'leavelike/create_user.html',{'form':form})


def auth_form(request):
	if request.user.is_authenticated():
		return redirect(reverse('entrys'))
	if request.method == 'POST':
		form = UserAuthForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect(reverse('entrys'))
			else:
				return redirect(reverse('auth-user'))
		else:
			return redirect(reverse('auth-user'))
	else:
			form = UserAuthForm()
	return render(request,'leavelike/authuser.html',{'form':form})


def print(request):
	line = "You can't edit post another users"
	return render(request,'leavelike/foredit.html',{'line':line})


def dislog(request):
	logout(request)
	return redirect(reverse('auth-user'))