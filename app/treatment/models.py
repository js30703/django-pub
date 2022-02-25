from django.db import models
from datetime import datetime
from utills.uuid import CustomUUIDField
from app.base.models import BaseModel
from app.authentication.models import BracHChoice


class Service(BaseModel):
    uuid = CustomUUIDField(unique=True)
    code = models.CharField("code", max_length=50)
    name = models.CharField("name", max_length=50)
    list_price = models.PositiveIntegerField("price")
    share_doctor = models.FloatField("share_doctor")
    share_employee = models.PositiveIntegerField("share_employee")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = verbose_name
        ordering = ['code']

    def __str__(self):
        return f"[{self.code}] {self.name}"


class Product(BaseModel):  # 이빨
    uuid = CustomUUIDField(unique=True)
    teeth = models.CharField("teeth", max_length=50)
    treatment = models.ForeignKey(
        "treatment.Treatment", verbose_name="treatment", on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(
        "treatment.Service", verbose_name="service", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("qantity", default=1)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.uuid}'


class TreatmentStatusChoice(models.TextChoices):
    A = 'Created', 'Created'
    B = 'Treated', 'Treated'
    D = 'Paid', 'Paid'


class Treatment(BaseModel):  # 다음 진료
    uuid = CustomUUIDField(unique=True)
    user = models.ForeignKey("authentication.User",
                             verbose_name="docotr", on_delete=models.CASCADE)
    patient = models.ForeignKey(
        "patient.Patient", verbose_name="patient", on_delete=models.CASCADE, null=True, blank=True)
    treatment_time = models.DateTimeField("treatment schedule", null=True)
    updated_date = models.DateTimeField("updated date", auto_now=True)
    next_treatement = models.CharField(
        "next_treatment", max_length=250, blank=True, null=True)
    diagnosis = models.CharField("diagnosis", max_length=50)
    employee = models.CharField(
        'payed_man', max_length=200, null=True, blank=True)
    total_amount = models.PositiveIntegerField(
        "total amount", default=0, blank=True, null=True)
    paid_amount = models.PositiveIntegerField(
        "paid amount", default=0, blank=True, null=True)
    status = models.CharField(
        max_length=50, choices=TreatmentStatusChoice.choices, default='Created')
    branch = models.CharField(max_length=50, choices=BracHChoice.choices,
                              default=None,
                              null=True
                              )

    invoice = models.FileField(
        "invoice", upload_to=f"invoice/{datetime.now().strftime('%Y-%m')}/", null=True, blank=True)

    class Meta:
        verbose_name = "Treatment"
        verbose_name_plural = verbose_name
        ordering = ('-treatment_time',)

    def __str__(self):
        return f"[{self.treatment_time.strftime('%d-%m-%Y %H:%M')}]{self.patient.name}"
