from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Employee, Manager, User

class EmployeeRegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address',widget=forms.TextInput(

		attrs = { 'class': 'form_control'}
))

	class Meta:
		model = User
		fields = ("email", "password1", "password2", 'company_id')
	def __init__(self, *args, **kwargs):
		super(EmployeeRegistrationForm,self).__init__(*args, **kwargs)
		self.fields['password1'].widget.attrs.update({'class' : 'form_control'})
		self.fields['password2'].widget.attrs.update({'class' : 'form_control'})
		self.fields['company_id'].widget.attrs.update({'class' : 'form_control'})


class ManagerRegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address',widget=forms.TextInput(

		attrs = { 'class': 'form_control'}
))

	class Meta:
		model = User
		fields = ("email", "password1", "password2", "company_id")
	
	def __init__(self, *args, **kwargs):
		super(ManagerRegistrationForm,self).__init__(*args, **kwargs)
		self.fields['password1'].widget.attrs.update({'class' : 'form_control'})
		self.fields['password2'].widget.attrs.update({'class' : 'form_control'})
		self.fields['company_id'].widget.attrs.update({'class' : 'form_control'})

class EmpoyeeAuthenticationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget = forms.PasswordInput (

		attrs = { 'class': 'loginform'}
))


	class Meta:
		model = User
		fields = ('email', 'password',)

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid Login")
	
	def __init__(self, *args, **kwargs):
		super(EmpoyeeAuthenticationForm,self).__init__(*args, **kwargs)
		
		self.fields['email'].widget.attrs.update({'class' : 'loginform'})
		self.fields['password'].widget.attrs.update({'class' : 'loginform'})

class ManagerAuthenticationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget = forms.PasswordInput(

		attrs = { 'class': 'loginform'}
))

	class Meta:
		model = User
		fields = ('email', 'password')
	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid Login")
	def __init__(self, *args, **kwargs):
		super(ManagerAuthenticationForm,self).__init__(*args, **kwargs)
		
		self.fields['email'].widget.attrs.update({'class' : 'loginform'})
		self.fields['password'].widget.attrs.update({'class' : 'loginform'})
