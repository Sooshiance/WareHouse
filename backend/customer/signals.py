from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import User, Customer


@receiver(pre_save, sender=User)
def create_supplier(sender, instance, created, **kwargs):
    if created:
        user: User = instance
        if user.role == 1:
            new_supplier = Customer.objects.create(
                user=user,
                phone_number=user.phone,
                role=user.role,
            )
