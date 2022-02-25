from django.db import models
from app.base.models import BaseModel
from utills.uuid import CustomUUIDField


class PayMethonChoice(models.TextChoices):
    A = 'Cash', 'Cash'
    B = 'Credit Card', 'Credit Card'
    C = 'Bank Transfer 1', 'Bank Transfer 1'
    D = 'Bank Transfer 2', 'Bank Transfer 2'


class Payment(BaseModel):
    uuid = CustomUUIDField(null=True)
    treatment = models.ForeignKey(
        "treatment.Treatment", verbose_name="treatment", on_delete=models.CASCADE)
    pay_method = models.CharField(
        max_length=50, choices=PayMethonChoice.choices)
    paid_amount = models.PositiveIntegerField(
        "paid_amount", default=0, blank=True, null=True)
    # invoice = models.FileField("invoice", upload_to='payment/', null=True)

    def __str__(self):
        return f"{self.treatment.patient.name}"

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = verbose_name
        ordering = ('-treatment__treatment_time',)
