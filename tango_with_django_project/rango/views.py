from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category
from rango.models import Page



def index (request):

   category_list = Category.objects.order_by('-likes')[:5]
   context_dict = {'categories': category_list}
   return render(request, 'rango/index.html', context = context_dict)
	
def about (request):

   context = RequestContext(request)
   return render_to_response('rango/about.html', {}, context)

	
def show_category(request, category_name_slug):
    # Request our context from the request passed to us.
    context_dict = {}
    
    try:
        
        category = Category.objects.get(slug=category_name_slug)
        
       
        pages = Page.objects.filter(category=category)
        
        # Add our results list to the template context under name pages.
        context_dict['pages'] = pages
        
        context_dict['category'] = category

    except Category.DoesNotExist:
        
        context_dict['category'] = None
        context_dict['pages'] = None

    # Go render the resonse and return it to thee client.
    return render(request, 'rango/category.html', context_dict)
