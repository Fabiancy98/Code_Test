import uuid
import base64
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from rest_framework_simplejwt.tokens import RefreshToken

EMPLOYEE_STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=12, unique=True, primary_key=True, editable=False)
    email = models.EmailField(verbose_name=_('email address'), unique=True, max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=EMPLOYEE_STATUS, default='Active')
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD="email"

    REQUIRED_FIELDS=["first_name"]

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh=RefreshToken.for_user(self)
        return{
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    
    def save(self, *args, **kwargs):
        if not self.id:
            # Generate a shorter base64-encoded UUID
            hex_string = uuid.uuid4().hex
            bytes_data = bytes.fromhex(hex_string)
            data = base64.urlsafe_b64encode(bytes_data).decode('ascii')[:12]
            self.id = data.replace("-","").replace("_", "")
        super().save(*args, **kwargs)
