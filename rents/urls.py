from django.urls import path, include
from .views import Rent_view

urlpatterns = [
	path('rent/<int:id>/', Rent_view.as_view(), name='rent')
]