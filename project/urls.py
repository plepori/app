from django.contrib import admin
from django.urls import path
from remo.views import home, scf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.as_view(), name="compara"),
    path('scf', scf.as_view(), name="scf"),
    ]
