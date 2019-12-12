from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
	{
		'author': 'Edward Yuen',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'December 10, 2019'
	},
	{
		'author': 'Vivian Mei',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'December 11, 2019'
	}
]

def home(request):
	context ={
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})