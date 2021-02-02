from django import forms
from django.contrib.auth.models import User
from basic_app.models import *
from django.views.generic import TemplateView, FormView
from django.contrib.auth import password_validation

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput, help_text=password_validation.password_validators_help_text_html())
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
	def clean(self):
		if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
			raise forms.ValidationError('Password are not equal')
		password_validation.validate_password(self.cleaned_data.get('password'), None)
		return self.cleaned_data

	class Meta():
		model = User
		fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('portfolio_site','profile_pic')