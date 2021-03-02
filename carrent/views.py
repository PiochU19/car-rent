from django.shortcuts import render
from django.views import View
from cars.models import Car

class Home_view(View):
	template_name = 'home.html'
	context = {
		'title': 'Home',
	}

	def get(self, request):
		queryset = Car.objects.filter(to_rent=True)
		self.context['cars'] = queryset
		return render(request, self.template_name, self.context)


