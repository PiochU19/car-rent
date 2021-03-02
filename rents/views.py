from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect, reverse
from django.views import View
from cars.models import Car
from .forms import RentForm
from .models import Rent

@method_decorator(login_required, name='dispatch')
class Rent_view(View):
	template_name = 'rent.html'

	form = RentForm

	context = {
		'title': 'Rent',
		'form': form,
	}
	def get(self, request, id):
		self.car = get_object_or_404(Car, pk=id)
		self.context['car'] = self.car
		return render(request, self.template_name, self.context)

	def post(self, request, id):
		self.form = RentForm(request.POST)

		if self.form.is_valid():
			rent = self.form.save(commit = False)
			rent.user = request.user
			rent.car = get_object_or_404(Car, pk=id)
			self.form.save()

			return redirect('/')
		return render(request, self.template_name, self.context)

