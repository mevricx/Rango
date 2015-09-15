from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says: Hello world! <a href='/rango/about'>About</a>")

def about(request):
	return HttpResponse("Things and such. Back to <a href="/rango/">Index</a>")
