from django.shortcuts import render
from cars.models import Carro

# Create your views here.

def view_cars(request):
    search = request.GET.get('search')
    if search:
        cars = Carro.objects.filter(modelo__icontains=search).order_by('modelo')
    else:
        cars = Carro.objects.all().order_by('modelo')

    return render(request,
                  'cars.html',
                  {'carrinhos': cars}
                  )
