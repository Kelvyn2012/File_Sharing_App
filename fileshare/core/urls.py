from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.upload_file, name="upload_file"),
    path("file/<uuid:uuid>/", views.file_detail, name="file_detail"),
    path('my-files/', views.my_files, name='my_files'),

]
