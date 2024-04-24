import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

User_Choice = (
    ('Admin', 'Admin'),
    ('Waitress', 'Waitress'),
    ('Customer', 'Customer'),
)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=20, choices=User_Choice, default='Customer')
    phone_number = models.CharField(max_length=13, unique=True)

    username = None

    USERNAME_FIELD = 'phone_number'
    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
