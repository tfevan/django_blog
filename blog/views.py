from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):

	return HttpResponse("hi") 


def detail(request, pk):
	return HttpResponse("hi %s" % pk)

def result(request, pk):
	return HttpResponse('l')