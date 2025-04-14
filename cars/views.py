from django.shortcuts import render, redirect
from cars.models import Carro
from cars.forms import CarModelForm

# Create your views here.

def view_cars(request):
    search = request.GET.get('search')
    if search:
        cars = Carro.objects.filter(modelo__icontains=search).order_by('modelo')
    else:
        cars = Carro.objects.all().order_by('modelo')

    return render(request,
                  'cars.html',
                  {'cars': cars}
                  )

def form_new_car(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('lista_carro')
    else:
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', { 'new_car_form': new_car_form })
    
