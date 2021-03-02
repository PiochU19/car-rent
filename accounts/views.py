from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .forms import UserSignupForm, ClientSignupForm
from .models import Client
from django.contrib.auth.models import User

class SignupView(View):
	template_name = 'signup.html'

	UserForm = UserSignupForm

	ClientForm = ClientSignupForm

	context = {
		'title': 'Signup',
		'UserForm': UserForm,
		'ClientForm': ClientSignupForm
	}
	def get(self, request):
		return render(request, self.template_name, self.context)

	def post(self, request):
		self.UserForm = UserSignupForm(request.POST)
		self.ClientForm = ClientSignupForm(request.POST, request.FILES)
		if self.UserForm.is_valid() and self.ClientForm.is_valid():
			user = User.objects.create_user(username=request.POST['username'] ,first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password = request.POST['password1'])
			client = self.ClientForm.save(commit=False)
			client.user = user
			self.ClientForm.save()
			return redirect('/log_in/')
		#else:
			#self.UserForm = UserClientSignupForm()
			#self.ClientForm = ClientSignupForm()
		return HttpResponse(self.ClientForm.errors)