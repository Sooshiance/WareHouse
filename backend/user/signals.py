from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from .models import User, Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        user: User = instance
        Profile.objects.create(
            user=user,
            email=user.email,
            phone=user.phone,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            role=user.role,
        )


@receiver(pre_save, sender=Profile)
def update_user(sender, instance: Profile, **kwargs):
    if instance.pk:
        user: User = instance.user
        user.phone = instance.phone
        user.username = instance.username
        user.email = instance.email
        user.first_name = instance.first_name
        user.last_name = instance.last_name
        user.save()


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)


post_delete.connect(delete_user, sender=Profile)
