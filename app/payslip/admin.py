from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import messages
from django.shortcuts import redirect
from app.authentication.models import User
from datetime import datetime
from django.contrib import admin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import path
from .models import PaySlip
from.calculate import payslip_doctor, payslip_employee


@admin.action(
    # permissions=['publish'],
    description='급여 명세 발행',
)
def issue_payslip(self, request, queryset):
    for payslip in queryset:
        if payslip.status == 'created':
            if payslip.user.type == 'Doctor':
                payslip_doctor(payslip)
            else:
                payslip_employee(payslip)


class PaySlipResource(resources.ModelResource):
    class Meta:
        model = PaySlip
        fields = ('id', 'pay_slip_date', 'user__name', "Type", "gross",
                  "basic_salary", "noon_shift", "overtime", "reward", "pdf")


@admin.register(PaySlip)
class PaySlipAdmin(ImportExportModelAdmin):
    list_display = ['user', 'status', 'pay_slip_date']
    list_filter = ['user__branch', ]
    actions = [issue_payslip]
    change_list_template = 'admin/payslip_list.html'
    resource_class = PaySlipResource

    def get_exclude(self, request, obj):
        if obj:
            if obj.type == 'Doctor':
                self.exclude = ['overtime', 'reward']
            else:
                self.exclude = ['noon_shift', 'assistant_fee']

        return self.exclude

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('empty_payslips/', self.empty_payslips),
        ]
        return my_urls + urls

    @transaction.atomic
    def empty_payslips(self, request):
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        if year and month:
            date = datetime(year=int(year), month=int(month), day=1)
            if not self.model.objects.filter(pay_slip_date=date).exists():
                for user in User.objects.filter(type__in=["Doctor", "Nurse", "Employee"]):
                    self.model.objects.create(
                        user=user,
                        status="created",
                        basic_salary=user.basic_salary,
                        pay_slip_date=date,
                        type=user.type
                    )
                messages.info(
                    request, f'payslips for {year}-{month} are created.')
            else:
                messages.warning(
                    request, f'payslips for {year}-{month} already exist.')
        else:
            messages.warning(
                request, f'please input date to issue payslips')
        return redirect("../")
