from django.urls import path
from api.views import ManageFileView, UploadView

urlpatterns = [
    path("upload", UploadView.as_view(), name="upload-file"),
    path("create-link", ManageFileView.as_view(), name="create-link"),
]
