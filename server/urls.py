from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("web/", include("web.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)