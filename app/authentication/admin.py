from django.contrib import admin
from .models import User, Group
from app.payslip.models import PaySlip
from datetime import datetime


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'type']
    list_filter = ['branch']
    list_per_page = 14


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
