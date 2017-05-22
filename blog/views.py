from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Category, Post


def home(request):
	post_list = Post.objects.all()
	pagination = Paginator(post_list, 2)

	page = request.GET.get('page')
	try:
		posts = pagination.page(page)
	except PageNotAnInteger:
		posts = pagination.page(1)
	except EmptyPage:
		posts = pagination.page(pagination.num_pages)

	return render(request, 'blog/index.html', {'posts': posts}) 


def detail(request, pk):
	return HttpResponse("hi %s" % pk)

def result(request, pk):
	return HttpResponse('l')