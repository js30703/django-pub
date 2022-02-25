from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    created = models.DateTimeField(verbose_name='created_time', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='updated_time', auto_now=True)

    class Meta:
        abstract = True

