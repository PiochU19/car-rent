from django.contrib import admin
from .models import Client, Employee, Headadmin

class ClientAdmin(admin.ModelAdmin):

	list_display = ('first_name', 'last_name', 'birth_date', 'city', 'username', 'email')

admin.site.register(Client, ClientAdmin)

class EmployeeAdmin(admin.ModelAdmin):

	list_display = ('first_name', 'last_name', 'birth_date', 'city', 'username', 'email')

admin.site.register(Employee, EmployeeAdmin)

class HeadadminAdmin(admin.ModelAdmin):

	list_display = ('first_name', 'last_name', 'birth_date', 'city', 'username', 'email')

admin.site.register(Headadmin, HeadadminAdmin)