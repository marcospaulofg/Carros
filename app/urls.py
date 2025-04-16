"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarListView, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import view_register, view_login, view_logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cars/", CarListView.as_view(), name="lista_carro"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car_update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car_delete"),
    path("new_car/", NewCarCreateView.as_view(), name="form_new_car"),
    path("register/", view_register, name='register'),
    path("login/", view_login, name='login'),
    path("logout/", view_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
