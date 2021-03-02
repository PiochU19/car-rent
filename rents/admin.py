from django.contrib import admin
from .models import Rent

class RentAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'brand', 'modell', 'rent_starts', 'rent_ends', 'additional_insurance', 'price')

admin.site.register(Rent, RentAdmin)