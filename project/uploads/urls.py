# uploads/urls.py
from django.urls import path
from .views import upload_file, user_files

urlpatterns = [
    path('', upload_file, name='upload_file'),
    path('my-files/', user_files, name='user_files'),
]