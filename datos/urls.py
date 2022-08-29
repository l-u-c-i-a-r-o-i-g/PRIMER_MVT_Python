from django.urls import path
from datos.views import test_familiares

urlpatterns = [
    path('', test_familiares ),
]


