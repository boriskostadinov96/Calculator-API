from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('admin/', views.admin_ui, name='admin_ui'),
]