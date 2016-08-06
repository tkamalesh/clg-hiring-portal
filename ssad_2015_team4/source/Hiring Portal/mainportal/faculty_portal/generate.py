#This module is used for generating the one-page summary

#ReportLab required modules are imported
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from time import time

from faculty_portal.models import Candidate,Application


def GenerateSummary(request):
	"""Creating one page summary for the application"""
	styles = getSampleStyleSheet()
	styleN = styles['Normal']
	styleM = styles['Heading3']
	styleH = styles['Heading2']
	story = []
	#Getting Candidate object to access required information.
	info = Candidate.objects.get(user_id=request.user.id)	
	#info = Candidate.objects.get(user_id = 2)
	
	infolist = [ ["Name",info.givenname], ["Age", info.age],["Institute of PhD",info.institue_of_phd],["Date of PhD Completion",info.date_of_completion],["Publication title-1",info.pub_title1], ["Publication title-2",info.pub_title2], ["Publication title-3",info.pub_title3], ["Publication title-4",info.pub_title4], ["Publication title-5",info.pub_title5] ]
	for information in infolist:
		story.append(Paragraph(information[0],styleH))
		story.append(Paragraph(str(information[1]),styleN))


	experience=[["Place",info.experience_place],["Position",info.experience_position],["Duration",info.experience_duration]]
	
	story.append(Paragraph("Experience -",styleH))

	for information in experience:
		story.append(Paragraph(information[0],styleM))
		story.append(Paragraph(information[1],styleN))


	fileinmodels="/"	
	filename = "static/uploaded_files/summary/"+str(time()).replace('.','_')+str(info.id)+".pdf"
	fileinmodels+=filename
	doc = SimpleDocTemplate(filename,pagesize = letter)
	doc.build(story)
	temp = Application.objects.get(candidate_id=info.id)
	temp.summarysheet=fileinmodels
	temp.save()

	# elements = []
 #    filename = str(str(user_id)+".pdf")
 #    doc = SimpleDocTemplate(filename, pagesize=landscape(A4))
 #    elements = basic_info(elements, user_id)  # ,pagesize)
 #    elements = other_info(elements, user_id)
 #    elements = chat_question(elements, user_id)
 #    elements = generate_certificate(elements)
 #    doc.build(elements, onFirstPage=myfirstpage, onLaterPages=mylaterpages)

 #    dat[0].append(str("First Name:"))
 #    dat[0].append(str(user.first_name))
	# data2 = [[Paragraph(cell, styles) for cell in row] for row in dat]
 #    t = Table(data2, colWidths=1.5 * inch, rowHeights=None, splitByRow=1, repeatRows=1, hAlign="RIGHT")
