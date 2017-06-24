from .models import Category, Post



def domain(request):
	return {
		'who': 'Django guru', 'name': 'Talha'

	}





def navbar(request):

	nav = Category.objects.all()[0:3]

	return {
			'navbar':nav
	}
