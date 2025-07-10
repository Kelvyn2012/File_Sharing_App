from django.shortcuts import render, redirect
from .forms import fileUploadForm
from .models import fileUpload

# Create your views here.


def upload_file(request):
    if request.method == "POST":
        form = fileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.owner = request.user
            file.save()
            return redirect("file details", uuid=file.share_uuid)
    else:
        form = fileUploadForm()
        return render(request, "core/upload.html", {form: form})
