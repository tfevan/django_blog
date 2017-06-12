
from django.shortcuts import render, get_object_or_404
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

	categories = Category.objects.all()

	return render(request, 'blog/index.html', {'posts': posts, 'page_range': page_range, 'categories':categories}) 


def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'blog/detail.html',{'post':post})








def result(request, pk):
	return HttpResponse('l')


def category(request, category_id):
	get = get_object_or_404(Category, id=category_id)

	category = get.post_set.order_by('published_date')

	paginator = Paginator(category, 1)

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	
	return render(request, 'blog/category.html', {'posts':posts})