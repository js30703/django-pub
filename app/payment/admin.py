from django.contrib import admin
from app.payment.create_invoice import create_invoice
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['treatment', 'created', 'paid_amount']
    actions = ['cancel_payment']
    list_per_page = 20

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('treatment', 'treatment__patient')

    @admin.action(description='cancel payment')
    def cancel_payment(self, request, queryset):
        for payment in queryset:
            uuid = payment.treatment.uuid
            payment.delete()
            create_invoice(uuid)
