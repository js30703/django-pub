from django.contrib import admin
from django.conf import settings
from django.urls import path, include  # add this
from django.utils.safestring import mark_safe

urlpatterns = [

    path("", include("app.survey.urls")),

]
