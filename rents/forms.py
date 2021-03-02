from django import forms
from .models import Rent

class RentForm(forms.ModelForm):
	rent_starts 				= forms.DateField(required = True,
									widget = forms.TextInput(
										attrs = {
											'class': 'inp',
											'id': 'datepicker_start',
											'placeholder': 'start',
											'onfocus': "(this.type='date')",
											'min': '01.01.1900',
											'max': '31.12.2020'}))

	rent_ends					= forms.DateField(required = True,
									widget = forms.TextInput(
										attrs = {
											'class': 'inp',
											'id': 'datepicker_end',
											'placeholder': 'ends',
											'onfocus': "(this.type='date')",
											'min': '01.01.1900',
											'max': '31.12.2020'}))

	price						= forms.IntegerField(required = True,
									widget = forms.NumberInput(
										attrs = {
											'hidden': 'true'}))

	additional_insurance		= forms.BooleanField(required = False,
									widget = forms.CheckboxInput(
										attrs = {
											'id': 'insurance'}))

	class Meta:
		model = Rent
		fields = ['rent_starts', 'rent_ends', 'price', 'additional_insurance']
