from django.contrib import admin
from django.urls import path
from remo.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('remo', home.as_view(), name="inicio"),
    ]
