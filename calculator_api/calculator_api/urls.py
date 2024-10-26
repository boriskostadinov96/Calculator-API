from django.contrib import admin
from django.urls import path, include
from api import views


def home_view(request):
    from django.http import HttpResponse
    return HttpResponse("Welcome to the Calculator API!")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', home_view, name='home'),
    path('api/', include('api.urls')),
]
