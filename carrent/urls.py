from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import Home_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Home_view.as_view(), name='home'),

    path('', include('accounts.urls')),
    path('', include('userprofile.urls')),
    path('', include('sets.urls')),
    path('ajax/', include('ajax.urls')),
    path('', include('rents.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
