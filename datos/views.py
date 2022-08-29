from django.http import HttpResponse
from django.template import loader
from datos.models import Familiar
from django.shortcuts import render

def test_familiares(request):
    queryset = Familiar.objects.all()
    dictionary = {'datos': queryset}
    plantilla = loader.get_template('familiares.html')
    documento_html = plantilla.render(dictionary)

    return HttpResponse(documento_html)