from random import randint, choice, choices
from datetime import datetime
from app.authentication.models import User
from app.payment.create_invoice import create_invoice
from app.treatment.models import Treatment, Service, Product
from app.payment.models import PayMethonChoice, Payment
from django.db.models import Prefetch
from django.db import transaction


def create_date():
    day = randint(1, 30)
    hour = randint(9, 22)
    minute = randint(0, 1)
    date = datetime(year=2022, month=1, day=day, hour=hour,
                    minute=0 if minute == 0 else 30)
    if date.weekday() in [5, 6]:
        return create_date()
    return date


def create_treatment():
    doctor_id_list = [2, 3, 5, 6, 7, 8, 4]
    for i in range(1, 100):
        id = randint(0, 6)
        doctor_id = doctor_id_list[id]
        Treatment.objects.create(user_id=doctor_id, patient_id=randint(
            10, 4031), treatment_time=create_date(), branch="SURABAYA")


def create_product():
    for treatment in Treatment.objects.filter(status='Created'):
        service_id_list = Service.objects.all().values_list('id', flat=True)
        repeat = choices([1, 2, 3, 4], [5, 2, 2, 1], k=1)[0]

        for i in range(0, repeat):
            service_id = choice(service_id_list)
            quantity = choices([1, 2, 3], [7, 2, 1], k=1)[0]
            Product.objects.create(
                teeth='teeth', service_id=service_id, treatment=treatment, quantity=quantity)
        treatment.status = 'Treated'
        treatment.save()


@transaction.atomic
def pay_treatment():
    for treatment in Treatment.objects\
        .select_related("user")\
        .prefetch_related(
            Prefetch('product_set', queryset=Product.objects.select_related('service').all()))\
            .filter(status='Treated', total_amount=0):
        total_amount = 0
        for product in treatment.product_set.all():
            total_amount += product.service.list_price * product.quantity

        Payment.objects.create(
            treatment=treatment,
            pay_method=choice(PayMethonChoice.choices)[0],
            paid_amount=total_amount,
        )
        treatment.total_amount = total_amount
        treatment.status = 'Paid'
        treatment.save()
        product.save()
        create_invoice(treatment.uuid)


if __name__ == "__main__":
    from create_dummy_treat import pay_treatment
    pay_treatment()
