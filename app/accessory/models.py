from typing import Text
from django.db import models
from utills.uuid import CustomUUIDField
from app.base.models import BaseModel
from django.utils.translation import gettext as _

class Accessory(models.Model):
    uuid = CustomUUIDField()
    name = models.CharField(_("name"), max_length=50)    
    stock = models.PositiveIntegerField(_("stock"))
    cost = models.PositiveIntegerField(_("cost"))
    
    class Meta:
        verbose_name = _("Accessory")
        verbose_name_plural = verbose_name

    def __str__(self):
      return f"{self.name}"


class Supplier(models.Model):
    uuid = CustomUUIDField()
    name = models.CharField(_("name"), max_length=50)   
    phone = models.CharField(_("phone"), max_length=50)
    memo = models.TextField(_("memo"), blank=True )

    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")

    def __str__(self):
        return f"Supplier:{self.uuid}"


class Procurement(BaseModel):
    uuid = CustomUUIDField()
    accessory = models.ForeignKey("accessory.Accessory", verbose_name=_("accessory"), on_delete=models.CASCADE)
    supplier = models.ForeignKey("accessory.Supplier", verbose_name=_("supplier"), on_delete=models.CASCADE)
    num = models.PositiveIntegerField(_("number"))
    cost = models.PositiveIntegerField(_("cost"))

    class Meta:
        verbose_name = _("Procurement")
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"Procurement:{self.uuid}"


class Sales(BaseModel):
    uuid = CustomUUIDField()
    accessory = models.ForeignKey("accessory.Accessory", verbose_name=_("accessory"), on_delete=models.CASCADE)
    num = models.PositiveIntegerField(_("number"))
    cost = models.PositiveIntegerField(_("cost"))
    price = models.PositiveIntegerField(_("pirce"))
    

    class Meta:
        verbose_name = _("Sales")
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"Sales:{self.uuid}"