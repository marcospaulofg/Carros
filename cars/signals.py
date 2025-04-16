from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Carro

@receiver(pre_save, sender=Carro)
def car_pre_save(sender, instance, **kwargs):
    print(f"Pre-save signal triggered for {instance}")

@receiver(post_save, sender=Carro)
def car_post_save(sender, instance, **kwargs):
    print(f"Post-save signal triggered for {instance}")

@receiver(pre_delete, sender=Carro)
def car_pre_delete(sender, instance, **kwargs):
    print(f"### Pre-delete signal triggered for {instance} ###")

@receiver(post_delete, sender=Carro)
def car_post_delete(sender, instance, **kwargs):
    print(f"### Post-delete signal triggered for {instance} ###")