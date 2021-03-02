from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms import MyAuthForm
from .views import SignupView

urlpatterns = [
	path('', include('django.contrib.auth.urls')),
	path('log_in/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=MyAuthForm), name='login'),
	path('signup/', SignupView.as_view(), name='signup')
]