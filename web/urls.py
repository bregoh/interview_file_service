from django.urls import path
from web.views import indexPage, uploadPage

urlpatterns = [
    path("", indexPage, name="home-page"),
    path("uploads", uploadPage, name="upload-page"),
]
