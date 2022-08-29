from django.http import HttpResponse
from django.template import loader
from datos.models import Familiar

def test_familiares(request):
    queryset = Familiar.objects.all()
    dictionary = {'familiares': queryset}
    template = loader.get_template('template.html')
    document_html = template.render(dictionary)
    return HttpResponse(document_html)