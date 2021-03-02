from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from accounts.models import Client, Employee, Headadmin
from accounts.forms import ClientSignupForm, EmployeeSignupForm, HeadadminSignupForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import PasswordChangingForm
from rents.models import Rent

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
	template_name = 'profile.html'

	context = {
		'title': 'Profile',
		'active_profile': 'active'
	}

	def get(self, request):
		return render(request, self.template_name, self.context)

@method_decorator(login_required, name='dispatch')
class ProfileEdit(View):
	template_name = 'edit_account.html'

	context = {
		'title': 'Edit profile',
		'active_profile_edit': 'active'
	}

	def get(self, request):
		user = request.user

		try:
			obj = Headadmin.objects.get(user=user.id)
			form = HeadadminSignupForm(request.POST or None, instance=obj)
		except Headadmin.DoesNotExist:
			pass

		try:
			obj = Client.objects.get(user=user.id)
			form = ClientSignupForm(request.POST or None, instance=obj)
		except Client.DoesNotExist:
			pass

		try:
			obj = Employee.objects.get(user=user.id)
			form = EmployeeSignupForm(request.POST or None, instance=obj)
		except Employee.DoesNotExist:
			pass

		self.context['form'] = form

		return render(request, self.template_name, self.context)

	def post(self, request):
		user = request.user
		try:
			obj = Headadmin.objects.get(user=user.id)
			form = HeadadminSignupForm(request.POST or None, instance=obj)
		except Headadmin.DoesNotExist:
			pass

		try:
			obj = Client.objects.get(user=user.id)
			form = ClientSignupForm(request.POST or None, instance=obj)
		except Client.DoesNotExist:
			pass

		try:
			obj = Employee.objects.get(user=user.id)
			form = EmployeeSignupForm(request.POST or None, instance=obj)
		except Employee.DoesNotExist:
			pass

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('profile'))

@method_decorator(login_required, name='dispatch')
class PasswordChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	template_name = 'password.html'
	success_url = reverse_lazy('profile')

@method_decorator(login_required, name='dispatch')
class RentsView(View):
	template_name = 'rents.html'
	rents = None

	context = {
		'active_rents': 'active',
		'title': 'Rents',
	}

	def get(self, request):
		user = request.user
		user_id = user.id
		self.rents = Rent.objects.all().filter(user=user_id)
		self.context['rents'] = list(self.rents)

		return render(request, self.template_name, self.context)

@method_decorator(login_required, name='dispatch')
def rent_delete(request, id):
	rent = get_object_or_404(Rent, pk=id)
	rent.delete()
	return HttpResponseRedirect(reverse('rents'))