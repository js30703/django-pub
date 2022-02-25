from django.contrib import admin
from .models import Accessory, Procurement, Supplier, Sales


@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display =['name','stock']
    list_per_page = 10
    
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display =['name','phone']
    list_per_page = 10
    


@admin.register(Procurement)
class ProcurementAdmin(admin.ModelAdmin):
    list_display =['accessory','num','cost']
    list_per_page = 10
    

    
@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display =['accessory','num','cost','price',]
    list_per_page = 10