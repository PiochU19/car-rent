from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

class PasswordChangingForm(PasswordChangeForm):
	old_password			= forms.CharField(required=True, widget=forms.PasswordInput(attrs={
								'placeholder': 'Old password',
								'class' : 'form-control form-control-right'}))
	new_password1			= forms.CharField(required=True, widget=forms.PasswordInput(attrs={
								'placeholder': 'Old password',
								'class' : 'form-control form-control-right'}))
	new_password2			= forms.CharField(required=True, widget=forms.PasswordInput(attrs={
								'placeholder': 'Old password',
								'class' : 'form-control form-control-right'}))

	class Meta:
		model = User
		fields = ['old_password', 'new_password1', 'new_password2']