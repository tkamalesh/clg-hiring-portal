from django import forms
from models import Candidate,Application

class ApplicationDetails(forms.ModelForm):
	class Meta:
		model = Candidate
		fields = ("givenname","surname","age","current_affliation","status_of_phd","institue_of_phd","date_of_completion","expected_date_of_completion","experience_place","experience_position","experience_duration","resume","cover_letter","pub_title1","publication1","pub_title2", "publication2","pub_title3", "publication3","pub_title4", "publication4","pub_title5", "publication5")
		widgets = {'givenname': forms.TextInput(attrs={'id': 'gname', 'required': True, 'placeholder': ''})
		,'surname': forms.TextInput(attrs={'id': 'sname', 'required': True, 'placeholder': ''})
		,'age': forms.NumberInput(attrs={'id': 'age', 'required': False, 'placeholder': ''})
		,'current_affliation': forms.TextInput(attrs={'id': 'cu_aff', 'required': False, 'placeholder': ''})
		,'institue_of_phd': forms.TextInput(attrs={'id': 'inst_phd', 'required': False, 'placeholder': ''})
		,'date_of_completion': forms.DateInput(attrs={'id': 'date_phd', 'required': False, 'placeholder': 'DD/MM/YYYY','format' : '%d/%m/%Y'})
		,'expected_date_of_completion': forms.DateInput(attrs={'id': 'exp_date_phd', 'required': False, 'placeholder': 'DD/MM/YYYY','format' : '%d/%m/%Y'})
		,'experience_place': forms.TextInput(attrs={'id': 'eplace', 'required': False, 'placeholder': ''})
		,'experience_position': forms.TextInput(attrs={'id': 'epos', 'required': False, 'placeholder': ''})
		,'experience_duration': forms.TextInput(attrs={'id': 'etime', 'required': False, 'placeholder': ''})
		,'resume': forms.FileInput(attrs={'id': 'resume', 'required': True, 'placeholder': 'Upload Resume'})
		,'cover_letter': forms.FileInput(attrs={'id': 'cletter', 'required': True, 'placeholder': 'Upload Cover Letter'})
		,'pub_title1': forms.TextInput(attrs={'id': 'pub_title1', 'required': False, 'placeholder': ''})
		,'publication1': forms.FileInput(attrs={'id': 'pub1', 'required': False, 'placeholder': 'Upload'})
		,'pub_title2': forms.TextInput(attrs={'id': 'pub_title2', 'required': False, 'placeholder': ''})
		,'publication2': forms.FileInput(attrs={'id': 'pub2', 'required': False, 'placeholder': 'Upload'})
		,'pub_title3': forms.TextInput(attrs={'id': 'pub_title3', 'required': False, 'placeholder': ''})
		,'publication3': forms.FileInput(attrs={'id': 'pub3', 'required': False, 'placeholder': 'Upload'})
		,'pub_title4': forms.TextInput(attrs={'id': 'pub_title4', 'required': False, 'placeholder': ''})
		,'publication4': forms.FileInput(attrs={'id': 'pub4', 'required': False, 'placeholder': 'Upload'})
		,'pub_title5': forms.TextInput(attrs={'id': 'pub_title5', 'required': False, 'placeholder': ''})
		,'publication5': forms.FileInput(attrs={'id': 'pub5', 'required': False, 'placeholder': 'Upload'})
		,}

class ResearchLabDetails(forms.ModelForm):
	class Meta:
		model = Application
		fields = ("applied_researchLab",)
		widgets = {"applied_researchLab" : forms.Select(attrs = {'class':'research_lab', 'required' : True}),}
