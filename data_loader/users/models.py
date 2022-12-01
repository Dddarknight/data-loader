from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    OUT = 'Out'
    BASIC = 'Basic'
    PREMIUM = 'Premium'
    ENTERPRISE = 'Enterprise'
    SUBSCRIBTION_CHOICES = [
        (OUT, 'Out'),
        (BASIC, 'Basic'),
        (PREMIUM, 'Premium'),
        (ENTERPRISE, 'Enterprise'),
    ]
    subscribe_plan = models.CharField(
        max_length=15,
        choices=SUBSCRIBTION_CHOICES,
        default=OUT,
    )
