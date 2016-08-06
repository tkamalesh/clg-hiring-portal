from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from form_module import *
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
from django import forms


from userroles.models import set_user_role
from userroles import roles


def login(request):
        if request.user.username:
                return HttpResponseRedirect('/faculty_portal')
        else:
                if request.method == 'POST':
                        username=request.POST.get('username','')
                        password=request.POST.get('password','')
                        user=auth.authenticate(username=username,password=password)
                        if user is not None and user.is_active:
                                auth.login(request,user)
				user_profile = get_object_or_404(UserProfile, user_id = user.id)
				print user_profile.first_timelogin
				if user_profile.first_timelogin is True:
					return HttpResponseRedirect('/faculty_portal/profile')
                                else:
					return HttpResponseRedirect('/faculty_portal')
                        else:
                                return HttpResponse('Invalid login. Please check again.')
                else:
                        c={}
                        c.update(csrf(request))
                        return render_to_response('authentication/login.html',c)

# Create your views here.

#def register(request):
#	if request.user.username:
#		return HttpResponseRedirect('/')
#	else:
#		if request.method == "POST":
#			form=RegistrationForm(request.POST)
#
#			if form.is_valid():
#				return HttpResponseRedirect('/success')
#		else:
#			form = RegistrationForm()
#		return render(request,'authentication/register',{form : 'form'})
# def register(request):
# 	if request.user.username:
# 		return HttpResponseRedirect('/faculty_portal/')
# 	else:
# 		if request.method == "POST":
# 			form=RegistrationForm(request.POST)

# 			if form.is_valid():
# 				user = form.save()
# 				user = auth.authenticate(username=request.POST['username'],password=request.POST['password1'])
# 				auth.login(request,user)
# 				return HttpResponse("Successful login ! :P")

# 			#else :
# 			#	return HttpResponse("Failed")
# 		else:
# 			form = RegistrationForm()
# 		#return render(request,'authentication/register.html',{form : 'form'})
# 		return render_to_response('authentication/register.html', {'form': form,},context_instance=RequestContext(request))


def register_success(request):
	return render_to_response('authentication/success.html',context_instance=RequestContext(request))

def SetCandidaterole(user):
	set_user_role(user, roles.candidate)


def register(request):
    args = {}
    args.update(csrf(request))

    if request.user.username:
    	return HttpResponseRedirect('/faculty_portal')
    else:
	    if request.method == 'POST':
	    	new_data = request.POST.copy()
	        form = RegistrationForm(request.POST)
	        args['form'] = form
	        print args
	        if form.is_valid(): 
	            form.save()  # save user to database if form is valid
	            
		    username = form.cleaned_data['username'] 
		    email = form.cleaned_data['email']

	            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]            
	            activation_key = hashlib.sha1(salt+email).hexdigest()            
	            key_expires = datetime.datetime.today() + datetime.timedelta(2)

	            #Get user by username

	            user=User.objects.get(username=username)

	            # Create and save user profile                                                                                                                                  
	            new_profile = UserProfile(user=user, activation_key=activation_key, 
	                key_expires=key_expires)
	            new_profile.save()

	            # Send email with activation key
	            email_subject = 'IIIT-Hyderabad - Account confirmation'
	            email_body = "Welcome to IIIT-Hyderabad's hiring portal.You have signed up. To activate your account, click this link within 48hours http://127.0.0.1:8000/accounts/confirm/%s" % (activation_key)

	            send_mail(email_subject, email_body, 'abhishek.vinjamoori@gmail.com',
	                [email], fail_silently=False)
		    print user.username
		    #user.is_active = False
		    #user.save()

		    #Candidate gets his role set.
		    SetCandidaterole(user)
		    if not user.is_active:
			    print "Not active %s"%(user.username)
		    else:
			    print "Active %s" %(user.username)
	            return HttpResponseRedirect('/accounts/register_success')
	    else:
	        args['form'] = RegistrationForm()

	    return render_to_response('authentication/register.html', args, context_instance=RequestContext(request))

@login_required
def logout(request):
	auth.logout(request)
	return redirect('authentication.views.register')

def register_confirm(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/faculty_portal')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        #return render_to_response('user_profile/confirm_expired.html')
        return HttpResponse("Your confirmation link has expired. Please register again.")
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.user
    user.is_active = True
    user.save()
    return render_to_response('authentication/confirm.html')
