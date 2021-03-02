from django.db import models

class Car(models.Model):
	brand					= models.CharField(max_length=40)
	model 					= models.CharField(max_length=40)
	generation				= models.CharField(max_length=10, null=True, blank=True)
	year_of_production		= models.IntegerField()
	fuel_type				= models.CharField(max_length=40)
	engine					= models.CharField(max_length=10)
	hourse_power			= models.CharField(max_length=10, default='0 hp')
	body_type				= models.CharField(max_length=40)
	seats					= models.IntegerField(default=5)
	doors					= models.IntegerField(default=5)
	acceleration 			= models.CharField(max_length=10)
	max_speed				= models.CharField(max_length=10)
	image					= models.ImageField(upload_to='carimages/')
	to_rent					= models.BooleanField(default=False)
	other_info				= models.TextField(blank=True)
	price					= models.IntegerField()

	class Meta:
		ordering = ('brand',)

	def __str__(self):
		return "{0} {1} {2} {3}".format(self.brand, self.model, self.generation, self.engine)