from django.db import models

from shortuuid.django_fields import ShortUUIDField

from user.models import User


class Supplier(models.Model):
    user           = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_supplier')
    company_name   = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=11)
    address        = models.CharField(max_length=255)
    is_approved    = models.BooleanField(default=False)
    sid            = ShortUUIDField(max_length=16, db_index=True, unique=True, alphabet="01234567abcdefg")

    def __str__(self):
        return self.company_name
