from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.

def current_location(request):
	t = loader.get_template('current_location_map.html')
	c = RequestContext(request)
	return HttpResponse(t.render(c))
