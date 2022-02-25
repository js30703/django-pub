from django.contrib import admin
from .models import Patient, Discount, Odontogram

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['name', 'gender', 'birth_date']
    list_display_links =['name']
    search_fields=['name', 'birth_date']
    exclude=['odontogram']
    pass




@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_per_page = 10
    pass


# @admin.register(Odontogram)
# class OdontogramAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     pass