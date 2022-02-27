import uuid
import random
import string
from django.utils import timezone
from django.db import models


class FilesManagement(models.Model):

    file_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to="media/uploads", null=False)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "filesmanagement"


class FileLinks(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    file = models.ForeignKey(
        FilesManagement, related_name="filelinks", on_delete=models.CASCADE
    )
    link = models.CharField(max_length=200)
    is_expired = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "filelinks"

    def save(self, *args, **kwargs):
        self.link = "".join(
            random.choices(string.ascii_lowercase + string.digits, k=15)
        )
        return super(FileLinks, self).save(*args, **kwargs)
