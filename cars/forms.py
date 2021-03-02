from django import forms
from .models import Car

class CarCreateForm(forms.ModelForm):
	brand						= forms.CharField(required=True,
									widget=forms.TextInput(
										attrs={
										'placeholder': 'Brand',
										'class': 'form-control',}))
	model						= forms.CharField(required=True,
									widget=forms.TextInput(
										attrs={
										'placeholder': 'Model',
										'class': 'form-control',}))
	generation					= forms.CharField(required=False,
									widget=forms.TextInput(
										attrs={
										'placeholder': 'Generation',
										'class': 'form-control',}))
	year_of_production			= forms.IntegerField(required=True,
									widget=forms.NumberInput(
										attrs={
										'placeholder': 'Year of production',
										'class': 'form-control',
										'min': 1950,
										'max': 2025,}))
	fuel_type					= forms.CharField(required=True,
									widget=forms.TextInput(
										attrs={
										'placeholder': 'Fuel type',
										'class': 'form-control',}))
	engine						= forms.CharField(required=True,
									widget=forms.TextInput(
										attrs={
										'placeholder': 'Engine',
										'class': 'form-control',
										'maxlength': 4,}))
	hourse_power				= forms.CharField(required=True,
									widget=forms.TextInput(
										attrs={
										'placeholder': 'Hourse power',
										'class': 'form-control',
										'maxlength': 7,}))
	body_type					= forms.CharField(required=True,
									widget=forms.TextInput(
										attrs={
										'placeholder': 'Body type',
										'class': 'form-control',}))
	seats						= forms.IntegerField(required=True,
									widget=forms.NumberInput(
										attrs={
										'placeholder': 'Seats',
										'class': 'form-control',}))
	doors						= forms.IntegerField(required=True,
									widget=forms.NumberInput(
										attrs={
										'placeholder': 'Doors',
										'class': 'form-control',}))
	acceleration				= forms.CharField(required=True,
									widget=forms.TextInput(
										attrs={
										'placeholder': 'Acceleration',
										'class': 'form-control',
										'maxlength': 6,}))
	max_speed					= forms.CharField(required=True,
									widget=forms.TextInput(
										attrs={
										'placeholder': 'Max speed',
										'class': 'form-control',
										'maxlength': 8,}))
	image						= forms.ImageField(required=True,
									widget=forms.FileInput(
										attrs={
										'class': 'file-input',}))
	to_rent						= forms.CharField(label='To rent', required=False,
									widget=forms.CheckboxInput(
										attrs={
										'class': 'check-input',}))
	other_info					= forms.CharField(required=False,
									widget=forms.TextInput(
										attrs={
										'placeholder': 'Other info',
										'class': 'form-control',}))
	price						= forms.IntegerField(required=True,
									widget=forms.NumberInput(
										attrs={
										'placeholder': 'Price',
										'class': 'form-control'}))



	class Meta:
		model = Car
		fields = ['brand', 'model', 'generation', 'year_of_production', 'fuel_type', 'engine', 'hourse_power', 'body_type', 'seats', 'doors', 'acceleration', 'max_speed', 'image', 'to_rent', 'other_info', 'price']