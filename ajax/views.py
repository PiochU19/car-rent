from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from accounts.models import Client, Employee, Headadmin
from django.contrib.auth.models import User
from cars.models import Car
from rents.models import Rent
from datetime import date, timedelta

def users(request):
	users = request.GET.get('user', None)

	if users == 'employee':
		all_users = Employee.objects.values()
		i = 0
		for x in list(all_users):
			user_id = x['user_id']
			us = User.objects.filter(id=user_id).values_list('first_name', 'last_name', 'username', 'email', 'is_active')
			all_users[i]['first_name'] = us[0][0]
			all_users[i]['last_name'] = us[0][1]
			all_users[i]['username'] = us[0][2]
			all_users[i]['email'] = us[0][3]
			all_users[i]['is_active'] = us[0][4]

			i =+ 1

	elif users == 'client':
		all_users = Client.objects.values()
		i = 0
		for x in list(all_users):
			user_id = x['user_id']
			us = User.objects.filter(id=user_id).values_list('first_name', 'last_name', 'username', 'email', 'is_active')
			all_users[i]['first_name'] = us[0][0]
			all_users[i]['last_name'] = us[0][1]
			all_users[i]['username'] = us[0][2]
			all_users[i]['email'] = us[0][3]
			all_users[i]['is_active'] = us[0][4]

			i =+ 1

	elif users == 'admin':
		all_users = Headadmin.objects.values()
		i = 0
		for x in list(all_users):
			user_id = x['user_id']
			us = User.objects.filter(id=user_id).values_list('first_name', 'last_name', 'username', 'email', 'is_active')
			all_users[i]['first_name'] = us[0][0]
			all_users[i]['last_name'] = us[0][1]
			all_users[i]['username'] = us[0][2]
			all_users[i]['email'] = us[0][3]
			all_users[i]['is_active'] = us[0][4]

			i =+ 1

	data = {
		'users': list(all_users),
	}

	return JsonResponse(data, safe=False)

def free_days(request):
	car_id = request.GET.get('car', None)

	days = []

	rents = Rent.objects.filter(car=car_id).values_list('rent_starts', 'rent_ends')

	for i in rents:
		s_date = i[0]
		e_date = i[1]

		delta = e_date - s_date
		k = 0
		for x in range(delta.days + 1):
			day = s_date + timedelta(days = k)
			days.append(day)
			k += 1

	data = {
		'days': list(days),
	}

	return JsonResponse(data, safe=False)