from django.shortcuts import render_to_response,get_object_or_404 , render
from django.template.context import RequestContext
from django.http import HttpResponse
import json
from .forms import EntradaForm
from .script import es_primo_circular

def home(request):
	template= 'index.html'
	form = EntradaForm()
	ctx = {'form': form}
	return render_to_response(template,ctx,context_instance= RequestContext(request))


def validar(request):
    to_json = {}
    to_json.update(success=False)

    if request.is_ajax():
    	numero =  request.POST.get('data')
    	if numero == "1":
    		return HttpResponse(json.dumps(to_json), content_type="application/json")
    	if es_primo_circular(numero):
    		to_json.update(success=True)
    return HttpResponse(json.dumps(to_json), content_type="application/json")