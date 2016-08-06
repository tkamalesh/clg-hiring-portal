from django.shortcuts import render,render_to_response,get_object_or_404
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from faculty_portal.models import Application,Candidate
from django.contrib.auth.decorators import login_required
from authentication.models import *
from userroles.decorators import role_required
from userroles import roles
from userroles.models import UserRole
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.utils import timezone
from django.utils.timesince import timesince


from forms import FacultylistForm
from Academic.Faculty.models import FacultyReview,Review

# Create your views here.

@login_required(login_url = '/faculty/login')
@role_required(roles.hiring_committee)
def index(request):
	candidatelist = Candidate.objects.all().filter(Q(application__allowed_level__gte = 2) | Q(application__allowed_level = -2))
	print candidatelist
	facultylist = []
	score=[]
	for i in candidatelist:
		filled = len(FacultyReview.objects.all().filter(application_id=i.application.id,filled_status=1))
		total = len(FacultyReview.objects.all().filter(application_id=i.application.id))
		facultylist+=[[filled,total]]
		if Application.objects.get(candidate_id=i.id).allowed_level < 4 and filled == total and total !=0:
			selected_application = Application.objects.get(candidate_id=i.id)
			selected_application.allowed_level = 4
			selected_application.save()
		appls = Review.objects.all().filter(applications_id=i.application.id)
		average = 0
		for j in appls:
			average += (j.strength + j.area_of_expertize + j.appropriateness + j.recommendation)/(1.0*4)
		if len(appls) != 0:
			average = average/(1.0*len(appls))
		else:
			average = -1
		score+=[average]
		print score
	candidate = zip(candidatelist,facultylist,score)
	context ={'candidate':candidate}
	return render(request, 'HiringCommittee/index.html', context)

@login_required(login_url = '/faculty/login')
@role_required(roles.hiring_committee)
def addfaculty(request,candidate_id):
        candidate = get_object_or_404(Candidate, user_id = candidate_id)
	#facultywithappls = FacultyReview.objects.all().filter(application_id = candidate.application.id)

	facultylist = UserRole.objects.all().filter(name = "faculty")
	facultynamelist = []
	for i in facultylist:
		u=User.objects.get(id = i.user_id)
		facultynamelist += [[u.first_name,u.last_name,u.id ]]
	
	#facultyform = FacultylistForm()
	#facultyform.fields['facultylist'].choices = [(x.user_id, x) for x in UserRole.objects.all().filter(name = "faculty") ]
	context ={'candidate':candidate, 'facultynamelist' : facultynamelist}
	return render(request, 'HiringCommittee/addfaculty.html', context)



@login_required(login_url = '/faculty/login')
@role_required(roles.hiring_committee)
def detail(request,candidate_id):

        print request.user.id,candidate_id
        #assert int(candidate_id) == int(request.user.id)
        candidate = get_object_or_404(Candidate, user_id = candidate_id)
        return render(request, 'HiringCommittee/detail.html', {'candidate': candidate})

@login_required(login_url = '/faculty/login')
@role_required(roles.hiring_committee)
def forward(request,candidate_id):
	cand = get_object_or_404(Candidate, user_id=candidate_id)
	try:
		selected_application = Application.objects.get(candidate_id=cand.id)
	except :
		return render(request, 'hiringcomindex', {'error_message': "Some problem",})
	else:
		selected_application.status = 1
		selected_application.allowed_level = 3
		selected_application.stage_waiting_time = timezone.now()
		selected_application.save()
		#print request.POST
		facultysend = request.POST.getlist('facultylist')
		print facultysend
		for faculty in facultysend:
			print faculty
			if FacultyReview.objects.all().filter(application_id = selected_application.id, faculty_id = faculty).count() == 0:
				reviewer = FacultyReview(application_id = selected_application.id, faculty_id = faculty)
				reviewer.save()
	    # Always return an HttpResponseRedirect after successfully dealing
	    # with POST data. This prevents data from being posted twice if a
	    # user hits the Back button.
		return HttpResponseRedirect(reverse('hiringcomindex'))
		

@login_required(login_url = '/faculty/login')
@role_required(roles.hiring_committee)
def interview(request,candidate_id):
	print "ASSAD"
	cand = get_object_or_404(Candidate, user_id=candidate_id)
	assert int(cand.application.allowed_level) == 4
	try:
		selected_application = Application.objects.get(candidate_id=cand.id)
	except :
		return render(request, 'hiringcomindex', {'error_message': "Some problem",})
	else:
		print "Inside here"
		selected_application.status = 2
		selected_application.allowed_level = 5
		selected_application.stage_waiting_time = timezone.now()
		selected_application.save()
	    # Always return an HttpResponseRedirect after successfully dealing
	    # with POST data. This prevents data from being posted twice if a
	    # user hits the Back button.
		return HttpResponseRedirect(reverse('hiringcomindex'))
		
@login_required(login_url = '/faculty/login')
@role_required(roles.hiring_committee)
def reject(request,candidate_id):
	cand = get_object_or_404(Candidate, user_id=candidate_id)
	try:
		selected_application = Application.objects.get(candidate_id=cand.id)
	except :
		return render(request, 'hiringcomindex', {'error_message': "Some problem",})
	else:
		selected_application.status = -1
		selected_application.allowed_level = -2 
		selected_application.save()
	    # Always return an HttpResponseRedirect after successfully dealing
	    # with POST data. This prevents data from being posted twice if a
	    # user hits the Back button.
		return HttpResponseRedirect(reverse('hiringcomindex'))



@login_required(login_url = '/faculty/login')
@role_required(roles.hiring_committee)
def review(request,candidate_id):
	candidate = get_object_or_404(Candidate, user_id = candidate_id)
	selected_application = Application.objects.get(candidate_id=candidate.id)
        appls = Review.objects.all().filter(applications_id=selected_application.id)
	return render(request, 'HiringCommittee/review.html', {'appls': appls})

