from django.contrib import admin
from django.conf import settings
from django.urls import path, include  # add this
from django.utils.safestring import mark_safe
from django.http import HttpResponse

from app.payslip.views import pay_slip_list


urlpatterns = [
    path('health/', lambda request: HttpResponse()),
    path("api/", include('api.urls')),
    path("patient/", include("app.patient.urls")),
    path("treatment/", include("app.treatment.urls")),
    path("payment/", include("app.payment.urls")),
    path("profile/", pay_slip_list),
    # Auth routes - login / register
    path("", include("app.authentication.urls")),

]
