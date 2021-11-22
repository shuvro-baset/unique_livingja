from django.db import models
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.safestring import mark_safe

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    AbstractUser,
)


class UniUser(AbstractUser):
    USER_TYPES = (
        ('Sales', _('Sales')),
        ('Customer', _('Customer')),
    )
    user_type = models.CharField(choices=USER_TYPES, null=True, blank=True, max_length=200, help_text=mark_safe('<h2 style="color: #008CBA;">Set user type if user is customer or sales.</h2>'))
