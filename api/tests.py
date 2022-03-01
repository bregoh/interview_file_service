from io import BytesIO
from uuid import UUID
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


def create_photo_file():
    data = BytesIO()
    Image.new("RGB", (100, 100)).save(data, "PNG")
    data.seek(0)
    return SimpleUploadedFile("photo.png", data.getvalue())


class FileSharingTest(APITestCase):

    file_id = None

    def test_user_can_upload_file(self):
        # create a new file data
        file = create_photo_file()

        # mock an api call
        response = self.client.post(reverse("upload-file"), {"files_to_upload": file})
        result = response.data["data"]
        self.file_id = result["file_id"]

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        uuid = UUID(self.file_id, version=4)
        self.assertEqual(uuid.hex, self.file_id.replace("-", ""))

    def test_link_is_valid(self):
        # create a new file data
        file = create_photo_file()

        # mock an api call
        response = self.client.post(reverse("upload-file"), {"files_to_upload": file})
        result = response.data["data"]
        self.file_id = result["file_id"]
        data = {"file_id": self.file_id, "password": "test"}

        self.assertIsNotNone(self.file_id)
        response = self.client.post(reverse("create-link"), data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
