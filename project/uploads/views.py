# uploads/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm
from .models import UploadedFile

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            return redirect('dashboard')
    else:
        form = FileUploadForm()
    return render(request, 'uploads/upload.html', {'form': form})

@login_required
def user_files(request):
    files = UploadedFile.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'uploads/show-files.html', {'files': files})