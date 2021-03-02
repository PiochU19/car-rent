from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
import re
from django.core.exceptions import ValidationError
from .models import Headadmin, Employee, Client


class DateInput(forms.DateInput):
	input_type = 'date'

class MyAuthForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ['username','password']
	def __init__(self, *args, **kwargs):
		super(MyAuthForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
		self.fields['username'].label = False
		self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}) 
		self.fields['password'].label = False

class UserSignupForm(forms.Form):
	username				= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'username',
										'class' : 'form-control form-control-left'}))

	password1				= forms.CharField(required = True,
								widget = forms.PasswordInput(
									attrs = {
										'placeholder' : 'password',
										'class' : 'form-control form-control-left'}))

	password2				= forms.CharField(required = True,
								widget = forms.PasswordInput(
									attrs = {
										'placeholder' : 'password',
										'class' : 'form-control form-control-left'}))

	first_name				= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'first name',
										'class' : 'form-control form-control-left'}))

	last_name				= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'last name',
										'class' : 'form-control form-control-left'}))

	email					= forms.EmailField(required = True,
								widget = forms.EmailInput(
									attrs = {
										'placeholder' : 'email',
										'class' : 'form-control form-control-left'}))
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		r = User.objects.filter(username=username)
		if r.count():
			raise  ValidationError("Username already exists")
		return username

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email=email)
		if r.count():
			raise  ValidationError("Email already exists")
		return email

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise ValidationError("Password don't match")

		return password2

class ClientSignupForm(forms.ModelForm):
	birth_date				= forms.DateField(required = True,  label="Birth_date",
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'birth date',
										'class' : 'form-control form-control-right',
										'onfocus': "(this.type='date')",
										'min': '01.01.1900',
										'max': '31.12.2020'}))

	pesel					= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'pesel',
										'class' : 'form-control form-control-right',
										'maxlength': 11,
										'minlength': 11}))

	id_number				= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'id number',
										'class' : 'form-control form-control-right',
										'maxlength': 7,
										'minlength': 7}))

	city					= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'city',
										'class' : 'form-control form-control-right'}))

	street					= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'street',
										'class' : 'form-control form-control-right'}))

	street_number			= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'street number',
										'class' : 'form-control form-control-right',
										'maxlength': 5}))

	postal_code				= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'postal code',
										'class' : 'form-control form-control-right',
										'maxlength': 6,
										'minlength': 6}))

	class Meta:
		model = Client
		fields = ['birth_date', 'pesel', 'id_number', 'city', 'street', 'street_number', 'postal_code']

class EmployeeSignupForm(forms.ModelForm):
	birth_date				= forms.DateField(required = True,  label="Birth_date",
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'birth date',
										'class' : 'form-control form-control-right',
										'onfocus': "(this.type='date')",
										'min': '01.01.1900',
										'max': '31.12.2020'}))

	pesel					= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'pesel',
										'class' : 'form-control form-control-right',
										'maxlength': 11,
										'minlength': 11}))

	id_number				= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'id number',
										'class' : 'form-control form-control-right',
										'maxlength': 7,
										'minlength': 7}))

	city					= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'city',
										'class' : 'form-control form-control-right'}))

	street					= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'street',
										'class' : 'form-control form-control-right'}))

	street_number			= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'street number',
										'class' : 'form-control form-control-right',
										'maxlength': 5}))

	postal_code				= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'postal code',
										'class' : 'form-control form-control-right',
										'maxlength': 6,
										'minlength': 6}))

	class Meta:
		model = Employee
		fields = ['birth_date', 'pesel', 'id_number', 'city', 'street', 'street_number', 'postal_code']

class HeadadminSignupForm(forms.ModelForm):
	birth_date				= forms.DateField(required = True,  label="Birth_date",
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'birth date',
										'class' : 'form-control form-control-right',
										'onfocus': "(this.type='date')",
										'min': '01.01.1900',
										'max': '31.12.2020'}))

	pesel					= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'pesel',
										'class' : 'form-control form-control-right',
										'maxlength': 11,
										'minlength': 11}))

	id_number				= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'id number',
										'class' : 'form-control form-control-right',
										'maxlength': 7,
										'minlength': 7}))

	city					= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'city',
										'class' : 'form-control form-control-right'}))

	street					= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'street',
										'class' : 'form-control form-control-right'}))

	street_number			= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'street number',
										'class' : 'form-control form-control-right',
										'maxlength': 5}))

	postal_code				= forms.CharField(required = True,
								widget = forms.TextInput(
									attrs = {
										'placeholder' : 'postal code',
										'class' : 'form-control form-control-right',
										'maxlength': 6,
										'minlength': 6}))

	class Meta:
		model = Headadmin
		fields = ['birth_date', 'pesel', 'id_number', 'city', 'street', 'street_number', 'postal_code']