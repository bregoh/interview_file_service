from rest_framework import serializers
from api.models import FileLinks, FilesManagement
from django.utils import timezone
from rest_framework.fields import Field


class TimeWithTimezoneField(Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        if not value:
            return None

        if isinstance(value, str):
            return value

        return timezone.make_naive(value, timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


class FileLinkSerializers(serializers.ModelSerializer):
    created = TimeWithTimezoneField(read_only=True)

    class Meta:
        model = FileLinks
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    filelinks = FileLinkSerializers(read_only=True, many=True)
    created = TimeWithTimezoneField(read_only=True)

    class Meta:
        model = FilesManagement
        fields = "__all__"
