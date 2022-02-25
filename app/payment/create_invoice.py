
from django.db.models import Prefetch
from app.treatment.models import Treatment, Product
from utills.pdf.draw_invoice import draw_invoice
from .models import Payment
import os
from django.core.files.base import ContentFile


def create_invoice(treatment_uuid):
    treatment = Treatment.objects.only('user__name', "patient__name", "treatment_time")\
        .select_related('user', 'patient')\
        .prefetch_related(
        Prefetch(
            'product_set',
            queryset=Product.objects.select_related('service').all(),
            to_attr='services'))\
        .get(uuid=treatment_uuid)
    # 기존 인보이스 지우기
    if treatment.invoice:
        treatment.invoice.delete()

    # 인보이스 그리기. 기존의 데이터 모두 가져와서
    date = treatment.treatment_time.date().strftime('%d-%m-%Y')
    treatment_table = [
        ['ID', 'DOCTOR', 'PATIENT', 'DATE'],
        [f'TR{treatment.uuid}', treatment.user.name,
            treatment.patient.name, date],
    ]

    service_detail = [
        ['CODE', 'NAME', 'QUANTITY', 'PRICE', ],
    ]
    total = 0
    for product in treatment.services:
        service_detail.append(
            [product.service.code, product.service.name,
                product.quantity, f'{product.service.list_price:,}', ]
        )
        total += product.service.list_price

    service_detail.append([])

    payment_detail = [
        ['DATE', 'METHOD', 'PAID AMOUNT', '', ],

    ]
    paid_total = 0
    for payment in Payment.objects.filter(treatment=treatment):
        payment_detail.append(
            [payment.created.date(), payment.pay_method,
             f'{payment.paid_amount:,}', '', ]
        )
        paid_total += payment.paid_amount

    payment_detail.append([])

    filename = f"{date.split('-')[0]}_{treatment.uuid}"

    original_file_path = draw_invoice(
        filename,
        treatment_table,
        service_detail,
        f"{total:,}",
        payment_detail,
        f"{paid_total:,}",
        f"{total - paid_total:,}")

    with open(original_file_path, "rb") as fh:
        with ContentFile(fh.read()) as file_content:
            treatment.invoice.save(f'{filename}.pdf', file_content)

    os.remove(original_file_path)
    del fh

    # 기존의 파일을 지울 수 있나?
    treatment.paid_amount = paid_total

    if treatment.total_amount == treatment.paid_amount:
        treatment.status = 'Paid'

    treatment.save()
