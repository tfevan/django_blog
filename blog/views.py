from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Category, Post


def home(request):
	post_list = Post.objects.order_by('published_date')
	pagination = Paginator(post_list, 1)

	page = request.GET.get('page')
	try:
		posts = pagination.page(page)
	except PageNotAnInteger:
		posts = pagination.page(1)
	except EmptyPage:
		posts = pagination.page(pagination.num_pages)

	index = posts.number - 1
	max_index = len(pagination.page_range)
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index - 3 else max_index

	page_range = pagination.page_range[start_index:end_index]

	return render(request, 'blog/index.html', {'posts': posts, 'page_range': page_range}) 


def detail(request, pk):
	return render(request, 'blog/detail.html')

def result(request, pk):
	return HttpResponse('l')