from django.urls import path, include
from .views import ProfileView, ProfileEdit, PasswordChangeView, RentsView, rent_delete

urlpatterns = [
	path('profile/', ProfileView.as_view(), name='profile'),
	path('profileedit/', ProfileEdit.as_view(), name='profile-edit'),
	path('password/', PasswordChangeView.as_view(), name='password'),
	path('rents/', RentsView.as_view(), name='rents'),
	path('rent_delete/<int:id>', rent_delete, name='rentdelete'),
]