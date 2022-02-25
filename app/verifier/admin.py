# from django.contrib import admin

# from app.verifier.tasks import task_test
# from app.verifier.models import EmailVerifier, PhoneVerifier


# @admin.register(EmailVerifier)
# class EmailVerifierAdmin(admin.ModelAdmin):
#     actions = ['t']

#     def t(self, request, queryset):
#         for obj in queryset:
#             pass
#             task_test.delay(obj.pk)
#     t.short_description = '테스크 로그 테스트'


# @admin.register(PhoneVerifier)
# class PhoneVerifierAdmin(admin.ModelAdmin):
#     pass

