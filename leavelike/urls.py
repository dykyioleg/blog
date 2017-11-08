from django.conf.urls import url
from .import views

urlpatterns = [
	#url(r'^$',views.get_text,name='entrys'),
	url(r'^$',views.GetTextList.as_view(),name='entrys'),
	#url(r'^([0-9]+)$',views.get_object,name='simple-entry'),
	url(r'^(?P<pk>[0-9]+)/$',views.GetObjectDetail.as_view(),name='simple-entry'),
	url(r'^([0-9]+)/likeup/',views.likeup,name='entry-likeup'),
	url(r'^([0-9]+)/addcomment/',views.addcomment,name='entry-addcom'),
	url(r'^([0-9]+)/delcomment/',views.delcomment,name='entry-delet'),
	url(r'^([0-9]+)/edit',views.editentry,name='entry-edit'),
	url(r'^create$',views.create_entry,name='create-entry'),
	url(r'^(?P<pk>[0-9]+)/delete',views.EntryDelete.as_view(),name='entry-delete'),
	url(r'^newuser$',views.createform, name='create-user'),
	url(r'^auth$',views.auth_form,name='auth-user'),
	url(r'^foredit$',views.print,name='for-edit'),
	url(r'^logout$',views.dislog,name='logout-user'),

]