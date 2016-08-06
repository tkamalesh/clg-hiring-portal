from django.shortcuts import render,render_to_response,get_object_or_404
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from .models import Application,Candidate
from form import *
from django.contrib.auth.decorators import login_required
from authentication.models import *
from userroles.decorators import role_required
from userroles import roles
from generate import GenerateSummary

# Create your views here.

@login_required(login_url='/accounts/login')
@role_required(roles.candidate)
def profile(request):
	if request.method == 'POST':
		form = ApplicationDetails(request.POST,request.FILES) #request.FILES takes care of the uploaded files
		form2 = ResearchLabDetails(request.POST)
		if form.is_valid and form2.is_valid:
			first = form.save(commit=False)
			print request.user.id,request.user.username
			first.user_id = request.user.id
			first.save()
			second = form2.save(commit=False)
			second.name = "Application"+str(first.id)
			second.candidate_id = first.id
			second.save()
			#One page summary generated
			GenerateSummary(request)
			#GenerateSummary(first,second)
			#The application will now be visible to the staff members
			
			
			temp=Candidate.objects.get(user_id = request.user.id)
			temp=Application.objects.get(candidate_id=temp.id)
			temp.allowed_level=1
			temp.save()
			changeState = UserProfile.objects.get(user_id = request.user.id)
			changeState.first_timelogin = False #From now on he will be redirected to his homepage and not the profile filling page.
			changeState.save()

			return HttpResponseRedirect('/faculty_portal')
	else:
		form = ApplicationDetails()
		form2 = ResearchLabDetails()
		args={}
		args.update(csrf(request))
		args['form'] = form
		args['form2'] = form2
		return render_to_response('faculty_portal/profile.html',args)


@login_required(login_url='/accounts/login')
@role_required(roles.candidate)
def index(request):

	candidate = get_object_or_404(Candidate, user_id = request.user.id)
	message="Welcome to IIIT's Faculty Hiring Portal"
	context = {'candidate': candidate}
	return render(request, 'faculty_portal/index.html', context)

@login_required(login_url='/accounts/login')
@role_required(roles.candidate)
def detail(request,candidate_id):

	print request.user.id,candidate_id
	assert int(candidate_id) == int(request.user.id)
        candidate = get_object_or_404(Candidate, user_id = candidate_id)
    	return render(request, 'faculty_portal/detail.html', {'candidate': candidate})

