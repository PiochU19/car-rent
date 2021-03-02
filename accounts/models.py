from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
	user 			= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

	birth_date		= models.DateField(blank=True)
	pesel			= models.CharField(max_length=11, blank=True)
	id_number		= models.CharField(max_length=10, blank=True)

	city			= models.CharField(max_length=30, blank=True)
	street			= models.CharField(max_length=30, blank=True)
	street_number	= models.CharField(max_length=5, blank=True)
	postal_code		= models.CharField(max_length=6, blank=True)

	is_client		= models.BooleanField(default=True)

	def first_name(self):
		return self.user.first_name

	def last_name(self):
		return self.user.last_name

	def username(self):
		return self.user.username

	def email(self):
		return self.user.email
		

class Employee(models.Model):
	user 			= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

	birth_date		= models.DateField(blank=True)
	pesel			= models.CharField(max_length=11, blank=True)
	id_number		= models.CharField(max_length=10, blank=True)

	city			= models.CharField(max_length=30, blank=True)
	street			= models.CharField(max_length=30, blank=True)
	street_number	= models.CharField(max_length=5, blank=True)
	postal_code		= models.CharField(max_length=6, blank=True)

	is_employee		= models.BooleanField(default=True)

	def first_name(self):
		return self.user.first_name

	def last_name(self):
		return self.user.last_name

	def username(self):
		return self.user.username

	def email(self):
		return self.user.email

class Headadmin(models.Model):
	user 			= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

	birth_date		= models.DateField(blank=True)
	pesel			= models.CharField(max_length=11, blank=True)
	id_number		= models.CharField(max_length=10, blank=True)

	city			= models.CharField(max_length=30, blank=True)
	street			= models.CharField(max_length=30, blank=True)
	street_number	= models.CharField(max_length=5, blank=True)
	postal_code		= models.CharField(max_length=6, blank=True)

	def first_name(self):
		return self.user.first_name

	def last_name(self):
		return self.user.last_name

	def username(self):
		return self.user.username

	def email(self):
		return self.user.email

	def superuser(self):
		return self.user.is_superuser