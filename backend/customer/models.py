from django.db import models

from user.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=255, blank=True, null=True)
    role = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.user.username
