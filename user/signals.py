from django.db.models.signals import post_save, post_delete

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
        

def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=UserAccount)


post_delete.connect(delete_user, sender=UserProfile)
