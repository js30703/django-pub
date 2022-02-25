from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models
from enum import Enum

from app.base.models import BaseModel
from safedelete.models import SafeDeleteMixin
from safedelete.managers import SafeDeleteManager,SafeDeleteAllManager, SafeDeleteDeletedManager
from safedelete.models import SOFT_DELETE_CASCADE
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _



class UserManager(SafeDeleteManager, DjangoUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.model.normalize_username(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class BracHChoice(models.TextChoices):
    A = 'SURABAYA','SURABAYA'
    B = "LOCATION2",'LOCATION2'

class UserTypeChoice(models.TextChoices):
    A = 'Supervisor','Supervisor'
    B = 'Doctor','Doctor'
    C = 'Nurse', 'Nurse'
    D = 'Employee', 'Employee'

class User(SafeDeleteMixin, AbstractUser):
    _safedelete_policy = SOFT_DELETE_CASCADE
    
    objects = UserManager()
    
    first_name = None
    last_name = None
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # 빈값 유지
    REGISTER_FIELDS = ['email','username', 'password']  # 회원가입 시 입력 받을 필드 (email, phone, password)

    name = models.CharField(verbose_name='name', max_length=50)
    email = models.EmailField(verbose_name='email', unique=True)
    phone = models.CharField(verbose_name='phone', max_length=11, null=True, blank=True)
    type = models.CharField(max_length=50,choices=UserTypeChoice.choices)
    basic_salary = models.PositiveIntegerField("basic salary", default=0)
    branch = models.CharField(max_length=50, choices=BracHChoice.choices)
    

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Group(Group):
    pass

    class Meta:
        app_label = 'authentication'
        verbose_name = _('gruop')
        verbose_name_plural = verbose_name