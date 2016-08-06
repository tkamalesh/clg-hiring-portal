from django.shortcuts import render,render_to_response,get_object_or_404
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from faculty_portal.models import Application,Candidate
from django.contrib.auth.decorators import login_required
from authentication.models import *
from userroles.decorators import role_required
from userroles import roles
from django.core.urlresolvers import reverse
from .models import Review,FacultyReview
from .form import ReviewForm

# Create your views here.

@login_required(login_url = '/faculty/login')
@role_required(roles.faculty)
def index(request):
	applicationlist = FacultyReview.objects.all().filter(faculty_id = request.user.id)
	#candidate = Candidate.objects.all().filter(application__allowed_level = 3)
	context ={'applicationlist': applicationlist}
	print applicationlist
	return render(request, 'Faculty/index.html', context)



@login_required(login_url = '/faculty/login')
@role_required(roles.faculty)
def detail(request,candidate_id):

        print request.user.id,candidate_id
        #assert int(candidate_id) == int(request.user.id)
        candidate = get_object_or_404(Candidate, user_id = candidate_id)
        return render(request, 'Faculty/detail.html', {'candidate': candidate})

@login_required(login_url = '/faculty/login')
@role_required(roles.faculty)
def review(request,candidate_id):
	if request.method == 'POST':
		form = ReviewForm(request.POST) 
		if form.is_valid:
			first = form.save(commit=False)
			cand = get_object_or_404(Candidate, user_id=candidate_id)
			assert int(cand.application.allowed_level) == 3
			mylist = FacultyReview.objects.all().filter(faculty_id = request.user.id)
			selected_application = get_object_or_404(Application, candidate_id = cand.id)
			myapplication = mylist.get(application_id = selected_application.id)
			assert myapplication.filled_status is False
			first.applications_id = selected_application.id
			first.save()
			
			#Saving that the faculty has filled the Review.
			reviewer = FacultyReview.objects.all().filter(application_id = selected_application.id)
			reviewer = reviewer.get(faculty_id = request.user.id)
			print reviewer
			reviewer.filled_status = True
			reviewer.save()
			#reviewer = FacultyReview(application_id = selected_application.id, faculty_id = request.user.id)
			#reviewer.save()
			
			return HttpResponseRedirect(reverse('facultyindex'))
	else:
		form = ReviewForm()
		args={}
		args.update(csrf(request))
		args['form'] = form
		cand = get_object_or_404(Candidate, user_id=candidate_id)
		assert int(cand.application.allowed_level) == 3
		args['candidate'] = cand
		return render_to_response('Faculty/review.html',args)

		
