from django.contrib import admin
from api.models import FileLinks, FilesManagement, UserAgent

# Register your models here.
admin.site.register(FilesManagement)
admin.site.register(FileLinks)
admin.site.register(UserAgent)
