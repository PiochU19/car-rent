from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect, reverse
from django.views import View
from accounts.models import Employee, Headadmin, Client
from django.contrib.auth.models import User
from accounts.forms import UserSignupForm, ClientSignupForm, EmployeeSignupForm, HeadadminSignupForm
from cars.models import Car
from cars.forms import CarCreateForm
from rents.models import Rent

user_staff_required = user_passes_test(lambda user: user.is_staff, login_url="/")

def staff_user(view_func):
	decorated_view_func = login_required(user_staff_required(view_func))
	return decorated_view_func

@method_decorator(staff_user, name='dispatch')
class UsersSettings(View):
	template_name = 'user_settings.html'
	context = {
		'title': 'Users settings',
		'active_users_settings': 'active',
	}

	def get(self, request):
		return render(request, self.template_name, self.context)

@method_decorator(staff_user, name='dispatch')
class UserDetail(View):
	template_name = 'user_detail.html'
	context = {
		'title': 'User',
	}

	def get(self, request, id):
		us = get_object_or_404(User, pk=id)
		try:
			obj = Headadmin.objects.get(user=id)
			self.context['obj'] = obj
			self.context['role'] = 'Admin'
		except Headadmin.DoesNotExist:
			pass
		try:
			obj = Client.objects.get(user=id)
			self.context['obj'] = obj
			self.context['role'] = 'Client'
		except Client.DoesNotExist:
			pass
		try:
			obj = Employee.objects.get(user=id)
			self.context['obj'] = obj
			self.context['role'] = 'Employee'
		except Employee.DoesNotExist:
			pass

		return render(request, self.template_name, self.context)

@method_decorator(staff_user, name='dispatch')
def user_delete(request, id):
	obj = get_object_or_404(User, pk=id)
	obj.delete()
	return redirect('/userssettings/')

@method_decorator(staff_user, name='dispatch')
class CreateUser(View):
	template_name = 'create_user.html'
	UserForm = UserSignupForm
	context = {
		'title': 'Create user',
		'UserForm': UserForm,
	}

	def get(self, request):
		return render(request, self.template_name, self.context)

	def post(self, request):
		user_type = request.POST.get('user_type')
		self.UserForm = UserSignupForm(request.POST)
		if self.UserForm.is_valid():
			if user_type == 'admin':
				user = User.objects.create_user(username=request.POST['username'] ,first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password = request.POST['password1'], is_superuser=True, is_staff=True)
				us = Headadmin(birth_date=request.POST['birth_date'], pesel=request.POST['pesel'], id_number=request.POST['id_number'], city=request.POST['city'], street=request.POST['street'], street_number=request.POST['street_number'], postal_code=request.POST['postal_code'])
				us.user = user
				us.save()
				return redirect('/userssettings/')
			if user_type == 'employee':
				user = User.objects.create_user(username=request.POST['username'] ,first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password = request.POST['password1'])
				us = Employee(birth_date=request.POST['birth_date'], pesel=request.POST['pesel'], id_number=request.POST['id_number'], city=request.POST['city'], street=request.POST['street'], street_number=request.POST['street_number'], postal_code=request.POST['postal_code'])
				us.user = user
				us.save()
				return redirect('/userssettings/')
			if user_type == 'client':
				user = User.objects.create_user(username=request.POST['username'] ,first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password = request.POST['password1'])
				us = Client(birth_date=request.POST['birth_date'], pesel=request.POST['pesel'], id_number=request.POST['id_number'], city=request.POST['city'], street=request.POST['street'], street_number=request.POST['street_number'], postal_code=request.POST['postal_code'])
				us.user = user
				us.save()
				return redirect('/userssettings/')

@method_decorator(staff_user, name='dispatch')
class UserEdit(View):
	template_name = 'user_edit.html'

	context = {
		'title': 'User edit',
	}

	def get(self, request, id):
		user_id = id
		get_object_or_404(User, pk=user_id)
		
		try:
			obj = Headadmin.objects.get(user=user_id)
			form = HeadadminSignupForm(request.POST or None, instance=obj)
		except Headadmin.DoesNotExist:
			pass

		try:
			obj = Client.objects.get(user=user_id)
			form = ClientSignupForm(request.POST or None, instance=obj)
		except Client.DoesNotExist:
			pass

		try:
			obj = Employee.objects.get(user=user_id)
			form = EmployeeSignupForm(request.POST or None, instance=obj)
		except Employee.DoesNotExist:
			pass
		self.context['obj'] = obj
		self.context['form'] = form

		return render(request, self.template_name, self.context)

	def post(self, request, id):
		user_id = id
		get_object_or_404(User, pk=user_id)
		
		try:
			obj = Headadmin.objects.get(user=user_id)
			form = HeadadminSignupForm(request.POST or None, instance=obj)
		except Headadmin.DoesNotExist:
			pass

		try:
			obj = Client.objects.get(user=user_id)
			form = ClientSignupForm(request.POST or None, instance=obj)
		except Client.DoesNotExist:
			pass

		try:
			obj = Employee.objects.get(user=user_id)
			form = EmployeeSignupForm(request.POST or None, instance=obj)
		except Employee.DoesNotExist:
			pass

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('user-detail', kwargs={'id': user_id}))

@method_decorator(staff_user, name='dispatch')
class CarsSettings(View):
	template_name = 'cars_settings.html'
	context = {
		'title': 'Cars settings',
		'active_cars_settings': 'active',
	}
	def get(self, request):
		queryset = Car.objects.all()
		self.context['cars'] = queryset
		return render(request, self.template_name, self.context)

@method_decorator(staff_user, name='dispatch')
class CarAdd(View):
	template_name = 'car_add.html'
	form = CarCreateForm
	context = {
		'form': form,
		'title': 'Add car'
	}
	def get(self, request):
		return render(request, self.template_name, self.context)

	def post(self, request):
		self.form = CarCreateForm(request.POST, request.FILES)
		if self.form.is_valid():
			self.form.save()
			self.form = CarCreateForm
			self.context['form'] = self.form
			return HttpResponseRedirect(reverse('cars-settings'))
		return render(request, self.template_name, self.context)

def car_delete(request, id):
	car = get_object_or_404(Car, pk=id)
	car.delete()
	return HttpResponseRedirect(reverse('cars-settings'))

@method_decorator(staff_user, name='dispatch')
class CarDetail(View):
	template_name = 'car_detail.html'
	context = {
		'title': 'Car detail',
	}
	def get(self, request, id):
		car = get_object_or_404(Car, pk=id)
		self.context['car'] = car
		return render(request, self.template_name, self.context)

@method_decorator(staff_user, name='dispatch')
class CarEdit(View):
	template_name = 'car_edit.html'
	form = CarCreateForm
	context = {
		'title': 'Car edit',
	}
	def get(self, request, id):
		car = get_object_or_404(Car, pk=id)
		self.form = CarCreateForm(None, instance=car)
		self.context['form'] = self.form
		return render(request, self.template_name, self.context)
	def post(self, request, id):
		car = get_object_or_404(Car, pk=id)
		self.form = CarCreateForm(request.POST, request.FILES, instance=car)
		if self.form.is_valid():
			self.form.save()
			return HttpResponseRedirect(reverse('car-detaiil', kwargs={'id': id}))
		return render(request, self.template_name, self.context)

@method_decorator(staff_user, name='dispatch')
class Rents_list_admin(View):
	template_name = 'rents_list_admin.html'
	queryset = Rent.objects.values()

	context = {
		'active_rents_settings': 'active',
		'title': 'Rents',
		'rents': queryset,
	}

	def get(self, request):
		self.context['rents'] = Rent.objects.all()

		return render(request, self.template_name, self.context)

@method_decorator(staff_user, name='dispatch')
def rent_delete(request, id):
	rent = get_object_or_404(Rent, pk=id)
	rent.delete()
	return HttpResponseRedirect(reverse('rents-list-admin'))
