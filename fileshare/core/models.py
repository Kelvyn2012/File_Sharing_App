from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
def user_directory_path(instance, file_name):
    return f"user_{instance.owner.id}/{file_name}"


class FileUpload(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    share_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    is_public = models.BooleanField(default=False)
    expire_after = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.file.name
