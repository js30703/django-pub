from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models

from app.base.models import BaseModel
from safedelete.models import SafeDeleteMixin
from safedelete.managers import SafeDeleteManager,SafeDeleteAllManager, SafeDeleteDeletedManager
from safedelete.models import SOFT_DELETE_CASCADE



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


class User(SafeDeleteMixin, AbstractUser):
    _safedelete_policy = SOFT_DELETE_CASCADE
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(verbose_name='이메일', unique=True)
    phone = models.CharField(verbose_name='휴대폰', max_length=11, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # 빈값 유지
    VERIFY_FIELDS = []  # 회원가입 시 검증 받을 필드 (email, phone)
    REGISTER_FIELDS = ['phone', 'password']  # 회원가입 시 입력 받을 필드 (email, phone, password)

    objects = UserManager()
    all_objects = SafeDeleteAllManager()
    deleted_objects = SafeDeleteDeletedManager()

    class Meta:
        verbose_name = '유저'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email

    def connect_device(self, uid, token):
        Device.objects.update_or_create(uid=uid, defaults={'user': self, 'token': token})

    def disconnect_device(self, uid):
        self.device_set.filter(uid=uid).delete()


class SocialKindChoices(models.TextChoices):
    KAKAO = 'kakao', '카카오'
    NAVER = 'naver', '네이버'
    FACEBOOK = 'facebook', '페이스북'
    GOOGLE = 'google', '구글'
    APPLE = 'apple', '애플'


class Social(BaseModel):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE)
    kind = models.CharField(verbose_name='타입', max_length=16, choices=SocialKindChoices.choices)

    class Meta:
        verbose_name = '소셜'
        verbose_name_plural = verbose_name


class Device(BaseModel):
    user = models.ForeignKey('authentication.User', verbose_name='유저', on_delete=models.CASCADE, null=True, blank=True)
    uid = models.CharField(verbose_name='UID', max_length=64, db_index=True)
    token = models.CharField(verbose_name='값', max_length=256)

    class Meta:
        verbose_name = '디바이스'
        verbose_name_plural = verbose_name
