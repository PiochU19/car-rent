from django.urls import path, include
from .views import (
	UsersSettings, UserDetail, user_delete, CreateUser, UserEdit,
	CarsSettings, CarAdd, car_delete, CarDetail, CarEdit,
	Rents_list_admin, rent_delete,
)

urlpatterns = [
	path('userssettings/', UsersSettings.as_view(), name='users-settings'),
	path('user/<int:id>/', UserDetail.as_view(), name='user-detail'),
	path('userdelete/<int:id>/', user_delete, name='user-delete'),
	path('createuser/', CreateUser.as_view(), name='create-user'),
	path('useredit/<int:id>/', UserEdit.as_view(), name='user-edit'),

	path('carssettings/', CarsSettings.as_view(), name='cars-settings'),
	path('caradd/', CarAdd.as_view(), name='car-add'),
	path('cardelete/<int:id>/', car_delete, name='car-delete'),
	path('car/<int:id>/', CarDetail.as_view(), name='car-detaiil'),
	path('caredit/<int:id>/', CarEdit.as_view(), name='car-edit'),

	path('rentssettings/', Rents_list_admin.as_view(), name='rents-list-admin'),
	path('rentdelete/<int:id>/', rent_delete, name='rent-delete'),
]