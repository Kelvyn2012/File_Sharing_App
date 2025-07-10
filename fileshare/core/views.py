from django.shortcuts import render, redirect, get_object_or_404
from .forms import FileUploadForm
from .models import FileUpload
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required


@login_required
def my_files(request):
    files = FileUpload.objects.filter(owner=request.user).order_by("-uploaded_at")
    return render(request, "core/my_files.html", {"files": files})


def home(request):
    return redirect("upload_file")


# Upload view
def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.owner = request.user
            file.save()
            return redirect("file_detail", uuid=file.share_uuid)
    else:
        form = FileUploadForm()

    return render(request, "core/upload.html", {"form": form})


# Detail view
def file_detail(request, uuid):
    file = get_object_or_404(FileUpload, share_uuid=uuid)
    return render(request, "core/file_detail.html", {"file": file})
