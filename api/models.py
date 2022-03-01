from datetime import date, datetime
import uuid
from django.utils import timezone
from django.db import models


class FilesManagement(models.Model):

    file_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to="media/uploads", null=False)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "filesmanagement"


class FileLinks(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    file = models.ForeignKey(
        FilesManagement, related_name="filelinks", on_delete=models.CASCADE
    )
    link = models.CharField(max_length=200)
    password = models.CharField(max_length=200, null=True)
    link_visit = models.IntegerField(default=0)
    is_expired = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "filelinks"


class UserAgent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    os = models.CharField(max_length=200)
    browser = models.CharField(max_length=200)
    link_id = models.UUIDField(null=True)

    class Meta:
        db_table = "useragent"
