from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {'variable':'value'})

def count(request):
	return render(request, 'count.html')