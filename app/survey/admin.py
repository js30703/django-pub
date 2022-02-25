from django.contrib import admin

from .models import ICF001,IFC001_2, ICF002



class IFC001_2Inline(admin.StackedInline):
    model = IFC001_2

@admin.register(ICF001)
class ICF001Admin(admin.ModelAdmin):
    list_display=['q1','q2', ]
    inlines = [IFC001_2Inline,]
    pass


@admin.register(ICF002)
class ICF002Admin(admin.ModelAdmin):
    list_display=['name','service', ]
    

# @admin.register(IFC001_2)
# class IFC001_2Admin(admin.ModelAdmin):
#     inlines = [ICF001Inline,]
    

