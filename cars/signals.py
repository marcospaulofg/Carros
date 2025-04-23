from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from cars.models import Carro, Inventario
from django.db.models import Sum
from ia_api.client import get_car_ai_bio

@receiver(pre_save, sender=Carro)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ai_bio = get_car_ai_bio(instance.modelo, instance.marca, instance.ano)
        instance.bio = ai_bio

def car_inventory_update():
    car_count = Carro.objects.all().count()
    car_value = Carro.objects.aggregate(total_value=Sum('preco'))['total_value']
    Inventario.objects.create(quantidade=car_count, valor=car_value)

@receiver(post_save, sender=Carro)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Carro)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()