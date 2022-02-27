from django.urls import path
from web.views import index, login, upload

urlpatterns = [
    path("", index, name="home-page"),
    path("login", login, name="login-page"),
    path("upload", upload, name="login-page"),
]
