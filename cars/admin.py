from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):

	list_display = ('brand', 'model', 'year_of_production', 'fuel_type', 'engine', 'body_type', 'to_rent')

	fieldsets = (
		('CAR INFO', {
			'fields': ('brand', 'model', 'generation', 'year_of_production', 'body_type', 'seats', 'doors')
		}),
		('ENGINE', {
			'fields': ('engine', 'hourse_power', 'fuel_type', 'acceleration', 'max_speed')
		}),
		('IMAGE', {
			'fields': ('image',)
		}),
		('OTHER', {
			'fields': ('to_rent', 'other_info', 'price')
		}),

	)

admin.site.register(Car, CarAdmin)