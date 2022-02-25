from django.db import models
from app.base.models import BaseModel

from utills.uuid import CustomUUIDField
from datetime import datetime


class PaySlip(BaseModel):
    user = models.ForeignKey("authentication.User",
                             verbose_name="person", on_delete=models.CASCADE)
    uuid = CustomUUIDField(unique=True)
    PAYSLIP_SATAUS = [
        ('created', 'created'),
        ('confirmed', 'confirmed'),
        ('delivered', 'delivered'),
    ]
    status = models.CharField(
        "status", choices=PAYSLIP_SATAUS, max_length=50, default='created')
    pdf = models.FileField(
        "payslip pdf", upload_to=f"payslip/{datetime.now().strftime('%Y')}/", blank=True)
    basic_salary = models.PositiveIntegerField("basic salary")
    pay_slip_date = models.DateField(
        "급여 기준일", auto_now=False, auto_now_add=False, null=True)
    modified_date = models.DateField("modified date", auto_now=True)
    gross = models.PositiveIntegerField("gross", blank=True, default=0)
    USER_TYPE_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Employee', 'Employee'),
    ]
    type = models.CharField(
        max_length=50,
        choices=USER_TYPE_CHOICES,
        default=None,
        null=True
    )
    noon_shift = models.PositiveIntegerField(
        "noon shift", help_text='for doctors', blank=True, default=0)
    overtime = models.PositiveIntegerField(
        "overtime", help_text='for nurses', blank=True, default=0)
    assistant_fee = models.PositiveIntegerField(
        "assistant fee", help_text='for doctors', blank=True, default=0)
    reward = models.PositiveIntegerField(
        "reward", help_text='for employees', blank=True, default=0)

    class Meta:
        verbose_name = "PaySlip"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name
