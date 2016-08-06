from django import forms
from django.core import validators
from .models import Review

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ("strength","area_of_expertize","appropriateness","recommendation","specific_recommendation","comments",)
		widgets = {'strength': forms.Select(attrs={'id': 'age', 'required': True})
		,'area_of_expertize': forms.Select(attrs={'id': 'area_of_expertize', 'required': True}),
		'appropriateness': forms.Select(attrs={'id': 'appropriateness', 'required': False}),
		'recommendation': forms.Select(attrs={'id': 'recommendation', 'required': True}),
		'specific_recommendation': forms.Textarea(attrs={'id': 'specific_recommendation', 'required': False, 'placeholder': 'Optional'}),
		'comments': forms.Textarea(attrs={'id': 'comments1', 'required': True, 'placeholder': ''})
		,}
