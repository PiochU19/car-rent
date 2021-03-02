from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

class Rent(models.Model):
	user 					= models.ForeignKey(User, on_delete=models.CASCADE)
	car 					= models.ForeignKey(Car, on_delete=models.CASCADE)
	rent_starts				= models.DateField()
	rent_ends				= models.DateField()
	additional_insurance	= models.BooleanField(default=False)
	price					= models.IntegerField()

	def first_name(self):
		return self.user.first_name

	def last_name(self):
		return self.user.last_name

	def brand(self):
		return self.car.brand

	def modell(self):
		return self.car.model