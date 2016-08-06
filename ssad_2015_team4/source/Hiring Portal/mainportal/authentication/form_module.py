from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","email", "password1", "password2")
        #start
        widgets = {'username': forms.TextInput(attrs={'id': 'Fname','class':'form-control' ,'required': True, 'placeholder': 'Username'})
		,'password1': forms.PasswordInput(attrs={'id': 'pwd', 'class':'form-control','required': True, 'placeholder': 'Password'})
		,'password2': forms.PasswordInput(attrs={'id': 'confpwd','class':'form-control', 'required': True, 'placeholder': 'Confirm Password'})
		,}

    def clean_email(self):
        email = self.cleaned_data["email"]
        print "Inside save method"
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')
    
    #modify save() method so that we can set user.is_active to False when we first create our user
    def save(self, commit=True):        
        print "Inside save method"
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        print commit
        if commit: 
            user.is_active = False # not active until he opens activation link
     	    print "User is not active"
            user.save()
        return user                 

