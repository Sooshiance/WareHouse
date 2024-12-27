from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import User, Supplier


@receiver(pre_save, sender=User)
def create_supplier(sender, instance, created, **kwargs):
    if created:
        user: User = instance
        if user.role == 2:
            new_supplier = Supplier.objects.create(
                user=user,
                contact_number=user.phone,
            )
