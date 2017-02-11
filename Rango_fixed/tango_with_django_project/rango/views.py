from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #construct a dictionary to pass to the template engine as its context
    #not the key bold message  is the same as in the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy cupcake!"}
    #return a rendered response to send to the client
    #We make use of the shortcut to make lfie easier 
    #Note that the first parameter is the template we wish to use
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')
# Create your views here.
