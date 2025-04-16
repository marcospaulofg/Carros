from cars.models import Carro
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView 

# Create your views here.

class CarListView(ListView):
    model = Carro
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('modelo')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(modelo__icontains=search)
        return cars

class CarDetailView(DetailView):
    model = Carro
    template_name = 'car_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Carro
    template_name = 'new_car.html'
    form_class = CarModelForm
    success_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Carro
    template_name = 'car_update.html'
    form_class = CarModelForm

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Carro
    template_name = 'car_delete.html'
    success_url = '/cars/'