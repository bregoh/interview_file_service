from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include, re_path

from web.views import loginPage

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        re_path(r"^view/(?P<file_id>.*)?$", loginPage, name="login-file"),
        path("web/", include("web.urls")),
        path("api/", include("api.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
