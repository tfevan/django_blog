from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post


def home(request):
	posts = Post.objects.all()
	return render(request, 'blog/index.html', {'posts': posts}) 


def detail(request, pk):
	return HttpResponse("hi %s" % pk)

def result(request, pk):
	return HttpResponse('l')