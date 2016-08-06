from django import forms


from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget,
        ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
	    Select2Widget
	    )

class FacultylistForm(forms.Form):
	facultylist = forms.MultipleChoiceField(widget=forms.SelectMultiple,label="Notify and subscribe faculty to this application:")

