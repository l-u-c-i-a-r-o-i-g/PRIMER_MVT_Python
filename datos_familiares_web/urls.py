from django.contrib import admin
from django.urls import path
from datos_familiares_web.views import test_familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familiares/', test_familiares),
]
