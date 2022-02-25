import os
from .models import PaySlip
from utills.pdf.draw_payslip import draw_payslip
from datetime import datetime, timedelta
from utills.date_caculate import get_previous_month_first, get_this_month_first
from app.treatment.models import Product, Service, Treatment
from django.core.files.base import ContentFile
from django.db.models import Sum


def payslip_doctor(payslip):

    total_doctor_commitssion = 0
    total_price = 0
    date = get_previous_month_first(payslip.pay_slip_date)
    last_date = get_this_month_first(payslip.pay_slip_date) - timedelta(days=1)

    # draw pay slip
    filename = f"{date.date().strftime('%Y-%m')}_{payslip.user}"
    pay_title = [
        ['PAYSLIP ID', 'NAME', 'TYPE', 'DATE'],
        [payslip.uuid, payslip.user.name, 'Doctor',
            f"{date.date().strftime('%Y-%m-%d')} ~ {last_date.date().strftime('%Y-%m-%d')}"]

    ]
    pay_detail = [
        ['DATE', 'TM ID', 'SERVICE', 'EA', 'PRICE', 'COMISSION'],  # product List
    ]
    if payslip.basic_salary != 0:

        pay_detail.append([
            '-',
            '-',
            'Basic Salary',
            1,
            '-',
            '{:,}'.format(payslip.basic_salary),
        ])
        total_doctor_commitssion += payslip.basic_salary

    # from service given this month * commission % (automatic)
    q = Product.objects.select_related('treatment', 'service')\
        .filter(
            treatment__user=payslip.user,
            treatment__treatment_time__gte=get_previous_month_first(
                payslip.pay_slip_date),
            treatment__treatment_time__lt=get_this_month_first(
                payslip.pay_slip_date),
    )

    for product in q:
        total_price += product.service.list_price * product.quantity
        total_doctor_commitssion += product.service.list_price * \
            product.service.share_doctor * product.quantity * 0.01
        # 윗줄은 진료와 상품 정보
        pay_detail.append([
            product.treatment.treatment_time.date().strftime('%m/%d'),
            product.treatment.uuid,
            f"{product.service.name}",
            product.quantity,
            '{:,}'.format(product.service.list_price * product.quantity),
            '{:,}'.format(int(product.service.list_price *
                          product.service.share_doctor * product.quantity * 0.01)),
        ])
        # 아래에 환자 이름
        pay_detail.append([
            '',
            '',
            f"   {product.treatment.patient.name}",
            '',
            '',
            '',
        ])

    # calculate
    if payslip.noon_shift != 0:
        pay_detail.append([
            '-',
            '-',
            'Noon Shift',
            payslip.noon_shift,
            '{:,}'.format(payslip.noon_shift*70_000),
            '{:,}'.format(payslip.noon_shift*70_000),
        ])

    total_doctor_commitssion += payslip.noon_shift*70_000
    total_price += payslip.noon_shift*70_000
    # Assistant Fee
    if payslip.assistant_fee != 0:
        pay_detail.append([
            '-',
            '-',
            'Assistant Fee',
            payslip.assistant_fee,
            '{:,}'.format(payslip.assistant_fee*150_000),
            '{:,}'.format(payslip.assistant_fee*150_000),
        ])

    total_doctor_commitssion += payslip.assistant_fee*150_000
    total_price += payslip.assistant_fee*150_000

    pay_detail.append([])

    product_total = ['{:,}'.format(total_price), '{:,}'.format(
        int(total_doctor_commitssion))]

    original_file_path = draw_payslip(
        filename, pay_title, pay_detail, product_total)

    with open(original_file_path, "rb") as fh:
        with ContentFile(fh.read()) as file_content:
            payslip.pdf.save(f'{filename}.pdf', file_content)
            payslip.status = 'confirmed'
            payslip.gross = total_doctor_commitssion
            payslip.save()

    os.remove(original_file_path)
    del fh


def payslip_employee(payslip):

    noon_shift = payslip.overtime
    total_nurse_commitssion = 0

    date = get_previous_month_first(payslip.pay_slip_date)
    last_date = get_this_month_first(payslip.pay_slip_date) - timedelta(days=1)

    # draw pay slip
    filename = f"[{date.date().strftime('%Y-%m')}]{payslip.user}"
    pay_title = [
        ['ID', 'NAME', 'type', 'DATE'],
        [payslip.uuid, payslip.user.name, payslip.user.type,
            f"{date.date().strftime('%Y-%m-%d')} ~ {last_date.date().strftime('%Y-%m-%d')}"]

    ]
    pay_detail = [
        ['DATE', 'TM ID', 'SERVICE', 'EA', 'PRICE', 'COMISSION'],  # product List
    ]
    if payslip.basic_salary != 0:
        pay_detail.append([
            date.date().strftime('%m/%d'),
            '-',
            'Basic Selery',
            1,
            '{:,}'.format(payslip.basic_salary),
            '{:,}'.format(payslip.basic_salary),
        ])
        total_nurse_commitssion += payslip.basic_salary

    pay_detail.append([
        date.date().strftime('%m/%d'),
        '-',
        'Food',
        1,
        '{:,}'.format(300_000),
        '{:,}'.format(300_000),
    ])
    total_nurse_commitssion += 300_000

    pay_detail.append([
        date.date().strftime('%m/%d'),
        '-',
        'Transport',
        1,
        '{:,}'.format(200_000),
        '{:,}'.format(200_000),
    ])
    total_nurse_commitssion += 200_000

    # Bonus
    q = Product.objects.select_related('treatment', 'service')\
        .filter(
            treatment__treatment_time__gte=get_previous_month_first(
                payslip.pay_slip_date),
            treatment__treatment_time__lt=get_this_month_first(
                payslip.pay_slip_date),
    )
    revenue = 0
    for product in q:
        revenue += product.service.list_price * product.quantity

    bonus = int(revenue * 0.0003)
    pay_detail.append([
        date.date().strftime('%m/%d'),
        '-',
        'Bonus',
        1,
        '-',
        '{:,}'.format(bonus),
    ])
    total_nurse_commitssion += bonus

    # over time
    if payslip.overtime != 0:
        pay_detail.append([
            date.date().strftime('%m/%d'),
            '-',
            'Overtime',
            payslip.overtime,
            '{:,}'.format(60_000),
            '{:,}'.format(payslip.overtime*60_000),
        ])

        total_nurse_commitssion += payslip.overtime*60_000

    if payslip.reward != 0:
        pay_detail.append([
            date.date().strftime('%m/%d'),
            '-',
            'Reward',
            payslip.reward,
            '{:,}'.format(50_000),
            '{:,}'.format(payslip.reward*50_000),
        ])

        total_nurse_commitssion += payslip.reward

    # 마무리

    pay_detail.append([])

    product_total = ['--', '{:,}'.format(int(total_nurse_commitssion))]

    original_file_path = draw_payslip(
        filename, pay_title, pay_detail, product_total)

    with open(original_file_path, "rb") as fh:
        with ContentFile(fh.read()) as file_content:
            payslip.pdf.save(f'{filename}.pdf', file_content)
            payslip.status = 'confirmed'
            payslip.gross = total_nurse_commitssion
            payslip.save()

    os.remove(original_file_path)
    del fh
