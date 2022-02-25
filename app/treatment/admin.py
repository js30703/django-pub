from django.contrib import admin
from .models import Treatment, Product, Service
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    readonly_fields = ('teeth', 'service', 'quantity')
    can_delete = False


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display_links = ('user', )
    list_display = ['id', 'user', 'patient',
                    'treatment_time', 'status', 'invoice', ]

    # readonly_fields = [
    #     'user','branch','patient','treatment_time',
    #     'status', 'paid_amount', 'uuid','pay_method','status',
    #     'pay_method','invoice','next_treatement','employee',
    #     'diagnosis'
    #     ]
    # list_display_links =['id']
    search_fields = ['user', 'uuid']
    list_filter = ['branch', 'status']
    inlines = [
        ProductInline,
    ]

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'treatment__treatment_time', 'service__list_price',
                  'service__name', 'service__code', "service__share_doctor", 'quantity', 'treatment__user__name',)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_per_page = 10
    resource_class = ProductResource


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = [
        'code',
        'name',
        'list_price',
        'share_doctor',
        'share_employee',
    ]
    readonly_fields = [
        'code',
        'name',
        'list_price',
        'share_doctor',
        'share_employee',
    ]
    list_display_links = ['name']
    search_fields = ['name', 'code']

    def has_delete_permission(self, request, obj=None):
        return False
