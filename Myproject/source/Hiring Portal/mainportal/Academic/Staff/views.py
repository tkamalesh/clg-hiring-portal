from django.shortcuts import render,render_to_response,get_object_or_404
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.utils import timezone
from django.utils.timesince import timesince

from faculty_portal.models import Application,Candidate
from authentication.models import *
from userroles.decorators import role_required
from userroles import roles

# Create your views here.



@login_required(login_url = '/faculty/login')
@role_required(roles.staff)
def index(request):
	#candidate = Candidate.objects.all().filter(application__allowed_level__gte = 1)
	candidate = Candidate.objects.all().filter(Q(application__allowed_level__gte = 1) | Q(application__allowed_level = -1))
	current_time = timezone.now 
	context ={'candidate':candidate,'currtime':current_time}
	return render(request, 'Staff/index.html', context)




@login_required(login_url = '/faculty/login')
@role_required(roles.staff)
def detail(request,candidate_id):

        print request.user.id,candidate_id
        #assert int(candidate_id) == int(request.user.id)
        candidate = get_object_or_404(Candidate, user_id = candidate_id)
        return render(request, 'Staff/detail.html', {'candidate': candidate})



@login_required(login_url = '/faculty/login')
@role_required(roles.staff)
def forward(request,candidate_id):
	cand = get_object_or_404(Candidate, user_id=candidate_id)
	try:
		selected_application = Application.objects.get(candidate_id=cand.id)
	except :
		return render(request, 'staffindex', {'error_message': "Some problem",})
	else:
		selected_application.status = 1
		selected_application.allowed_level = 2
		selected_application.stage_waiting_time = timezone.now()
		selected_application.save()
	    # Always return an HttpResponseRedirect after successfully dealing
	    # with POST data. This prevents data from being posted twice if a
	    # user hits the Back button.
		#return HttpResponseRedirect('/staff')
		return HttpResponseRedirect(reverse('staffindex'))
		

@login_required(login_url = '/faculty/login')
@role_required(roles.staff)
def reject(request,candidate_id):
	cand = get_object_or_404(Candidate, user_id=candidate_id)
	try:
		selected_application = Application.objects.get(candidate_id=cand.id)
	except :
		return render(request, 'staffindex', {'error_message': "Some problem",})
	else:
		selected_application.status = -1
		selected_application.allowed_level = -1 
		selected_application.save()
	    # Always return an HttpResponseRedirect after successfully dealing
	    # with POST data. This prevents data from being posted twice if a
	    # user hits the Back button.
		#return HttpResponseRedirect('/staff')
		return HttpResponseRedirect(reverse('staffindex'))
		

