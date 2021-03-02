from django.contrib import admin
from django.urls import path
from .views import users, free_days


urlpatterns = [
	path('users/', users, name='ajax-users'),
	path('days/', free_days, name='ajax-days')
]