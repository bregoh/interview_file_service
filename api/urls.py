from django.urls import path
from api.views import DeleteFileView, ManageFileView, UploadView

urlpatterns = [
    path("upload", UploadView.as_view(), name="upload-file"),
    path("create-link", ManageFileView.as_view(), name="create-link"),
    path("delete-file/<uuid:file_id>", DeleteFileView.as_view(), name="delete-file"),
]
