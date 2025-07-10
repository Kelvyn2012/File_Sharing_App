from django import forms
from .models import FileUpload  # Make sure your model class is named FileUpload


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ("file", "is_public", "expire_after")
        widgets = {
            "expire_after": forms.DateInput(attrs={"type": "date"}) 
        }
