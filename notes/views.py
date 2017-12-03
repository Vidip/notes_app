from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from models import user_profile ,  user_notes
from django.contrib.auth.models import User
import json 

# Create your views here.
def index(request):
	print "oyo"
	template = loader.get_template('note/index.html')
	context = ''
	return HttpResponse(template.render(context,request))
	#return render(request, 'notes/c.html','')

@csrf_exempt
def login(request):
	print "inside login func"
	print request.session.get('email')
	if request.session.get('email') is None:
		print "inside"
		message = False
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		print "user iss",user
		if user:
			profile = user_profile.objects.get(user=user)
			notes = user_notes.objects.filter(user=profile)
			request.session['email'] = profile.email
			print notes
			new_notes = []
			shared_notes= []
			for a in notes:
				print a
				if a.primary_user == True:
					new_notes.append(a)
				else:
					shared_notes.append(a)
			context = {
					"profile" : profile.name,
	                "notes": new_notes,
	                "shared_notes" : shared_notes
	        }
			return render(request, 'note/notes.html',context)
		else:
			print "wrong username and password"
			context = {
			'message' : 'Wrong Username or Password, please re-enter.'
			}
			return render(request, 'note/index.html',context)
	else:
		profile = user_profile.objects.get(email = request.session['email'])
		notes = user_notes.objects.filter(user=profile)
		new_notes = []
		shared_notes= []
		for a in notes:
			print a
			if a.primary_user == True:
				new_notes.append(a)
			else:
				shared_notes.append(a)
		context = {
				"profile" : profile.name,
	            "notes": new_notes,
	            "shared_notes" : shared_notes
	    }
		return render(request, 'note/notes.html',context)


@csrf_exempt
def sign_up(request):
	sign_up = False
	print request.POST['username']
	username = request.POST['username']
	password = request.POST['password']
	user = User.objects.filter(username = request.POST['username'])
	email = User.objects.filter(email = request.POST['email'])
	print user
	new_user = ''
	if user or email:
		print "username already exists"
		context = {
		"already" : True
		}
		return render(request, 'note/index.html',context)
	else:
		new_user = User.objects.create_user(username=request.POST['username'], email = request.POST['email'] , password =  request.POST['password'])
        if new_user:
	        profile = user_profile(user=new_user,name=request.POST['username'],email=request.POST['email'])
	        profile.save()
        context = {
        "sign_up" :True
        }
        return render(request, 'note/index.html',context)

def add_note(request):
	if request.session.get('email'):
		print request.session.get('email')
		note = request.POST['note']
		pro = user_profile.objects.get(email = request.session.get('email'))
		new_notes = user_notes(user=pro, note=note)
		new_notes.save()
		result = dict()
		notes = user_notes.objects.filter(user=pro)
		print notes
		new_notes = []
		shared_notes= []
		for a in notes:
			print a
			if a.primary_user == True:
				new_notes.append(a)
			else:
				shared_notes.append(a)
		context = {
				"profile" : pro.name,
                "notes": new_notes,
                "shared_notes" : shared_notes
        }
		return render(request, 'note/notes.html',context)

def delete_note(request,note_id):
	if request.session.get('email'):
		print request.session.get('email')
		print note_id
		pro = user_profile.objects.get(email = request.session.get('email'))
		user_notes(id=note_id).delete()
		result = dict()
		notes = user_notes.objects.filter(user=pro)
		print notes
		new_notes = []
		shared_notes= []
		for a in notes:
			print a
			if a.primary_user == True:
				new_notes.append(a)
			else:
				shared_notes.append(a)
		context = {
				"profile" : pro.name,
                "notes": new_notes,
                "shared_notes" : shared_notes
        }
		return render(request, 'note/notes.html',context)

def mark_note(request,note_id):
	if request.session.get('email'):
		print request.session.get('email')
		print note_id
		pro = user_profile.objects.get(email = request.session.get('email'))
		u_n = user_notes.objects.get(id=note_id)
		u_n.marked = True
		u_n.save()
		result = dict()
		notes = user_notes.objects.filter(user=pro)
		print notes
		new_notes = []
		shared_notes= []
		for a in notes:
			print a
			if a.primary_user == True:
				new_notes.append(a)
			else:
				shared_notes.append(a)
		context = {
				"profile" : pro.name,
                "notes": new_notes,
                "shared_notes" : shared_notes
        }
		return render(request, 'note/notes.html',context)

def open_note(request,note_id):
	if request.session.get('email'):
		list_of_users = []
		note = user_notes.objects.get(id=note_id)
		l_users = user_profile.objects.all()
		for i in l_users:
			if i.email != request.session.get('email'):
				list_of_users.append(i.name)
		context = {
		"notes" : note,
		"note_id" : note_id,
		"users" : list_of_users
		}
		return render(request, 'note/notes_page.html',context)

def user_logout(request):
	if request.session.get('email'):
		del request.session['email']
		request.session.modified = True
		logout(request)
		return HttpResponseRedirect('/')

def share_note(request,note_id):
	if request.session.get('email'):
		print note_id
		note = user_notes.objects.get(id=note_id)
		note_text = request.POST['note']
		note.note = note_text
		note.save()
		print note
		context = {
		"notes" : note,
		"note_id" : note_id
		}
		return render(request, 'note/notes_page.html',context)

def share_note_to_user(request,note_id):
	if request.session.get('email'):
		print note_id
		list_of_users = []
		l_users = user_profile.objects.all()
		for i in l_users:
			if i.email != request.session.get('email'):
				list_of_users.append(i.name)
		user_list = request.POST.getlist('user_name')
		note = user_notes.objects.get(id=note_id)
		new_note = note.note
		for i in user_list:
			print "inside for loop"
			user = user_profile.objects.get(name=i)
			print user
			if user_notes(user = user , original_note_id = note_id):
				print "aa"
			else:
				n = user_notes(note=new_note , primary_user = False, marked = False, user = user , original_note_id = note_id)
				n.save()
		context = {
		"notes" : note,
		"note_id" : note_id,
		"users" : list_of_users,
		"shared" : True
		}
		return render(request, 'note/notes_page.html',context)


def notes_profile(request):
	print "oyo"
	template = loader.get_template('note/notes.html')
	context = ''
	return HttpResponse(template.render(context,request))