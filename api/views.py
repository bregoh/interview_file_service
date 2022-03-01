from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, CreateAPIView, DestroyAPIView
from rest_framework import status
from api.models import FilesManagement
from api.serializers import FileLinkSerializers, FileSerializer
from api.service import generate_link
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_delete


class UploadView(ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES["files_to_upload"]
        name = file.name

        serializer = FileSerializer(data={"name": name, "file": file})
        if serializer.is_valid():
            serializer.save()

            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(
            {"error": str(serializer.error_messages)},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, *args, **kwargs):
        queryset = FilesManagement.objects.all()
        result = FileSerializer(queryset, many=True)

        return Response({"data": result.data}, status=status.HTTP_200_OK)


class ManageFileView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        file_id = request.data.get("file_id")
        password = request.data.get("password")

        link = generate_link(15)

        data = {"file": file_id, "link": f"view/{link}", "password": password}
        serializer = FileLinkSerializers(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(
            {"error": str(serializer.error_messages)},
            status=status.HTTP_400_BAD_REQUEST,
        )


class DeleteFileView(DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        file_id = kwargs["file_id"]
        FilesManagement.objects.filter(file_id=file_id).delete()
        return Response(
            {"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT
        )


@receiver(pre_delete, sender=FilesManagement)
def deleteImages(sender, instance, **kwargs):
    # parse False to prevent FileField from saving the model
    instance.file.delete(False)
