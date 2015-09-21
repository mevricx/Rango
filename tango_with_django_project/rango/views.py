from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	#return HttpResponse("Rango says: Hello world! <a href='/rango/about'>About</a>")
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Making your way in the world today takes everything you got!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context_dict)

def about(request):
	#return HttpResponse("Things and such. Back to <a href='/rango/'>Index</a>")
	context_dict = {'boldmessage': "Stuff and Things."}
	return render(request, 'rango/about.html', context_dict)
