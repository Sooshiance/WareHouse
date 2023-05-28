from django.db.models.signals import post_save

from .models import UserAccount, UserProfile


def create_profile(sender, instance, created, **kwargs):
    if created:
        user=instance
        new_profile = UserProfile.objects.create(
            user=user,
            email=user.email,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
        )


post_save.connect(create_profile, sender=UserAccount)
