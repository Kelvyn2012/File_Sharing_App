from django import forms
from .models import fileUpload


class fileUploadForm(forms.ModelForm):

    class Meta:
        model = fileUpload
        fields = (
            "file",
            "is_puplic",
            "expire_after",
        )
