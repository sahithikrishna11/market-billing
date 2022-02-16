from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path("billing/",include('market_billing.urls')),
    path('admin/', admin.site.urls),
]
