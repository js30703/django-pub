from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.utils.safestring import mark_safe
from django.contrib.auth.models import Group

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', admin.site.urls, name="admin"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "INDENTAL ADMIN"
admin.site.index_title = "Welcome to INDENTAL ADMIN"
admin.site.site_header = mark_safe(f'<img src="{settings.STATIC_URL + settings.SITE_LOGO}" height="88" style="vertical-align: bottom;" />') if settings.SITE_LOGO else f'{settings.SITE_NAME} 어드민'
admin.site.unregister(Group)
