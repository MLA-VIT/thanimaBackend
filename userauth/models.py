from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=128)
    reg_no = models.CharField(max_length=10, unique=True)
    contact = models.CharField(max_length=10, null=True, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    email_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6,default=000000)
    password = models.TextField()
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    username = models.CharField(max_length=128, default=uuid.uuid4, editable=False)
    verification_id = models.TextField()
    otp_validity = models.DateTimeField(null=True)
    verification_validity = models.DateTimeField(null=True)
    reg_complete = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contact','reg_no']

    def __str__(self):
        return self.email