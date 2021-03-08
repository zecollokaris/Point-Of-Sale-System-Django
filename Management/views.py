from django.shortcuts import render, redirect

from .models import *

from .forms import StockCreateForm 


#---------------------------------------------------------------------#
'''End Of Import'''
#---------------------------------------------------------------------#

# VIEW FUNCTIONS HERE!



#################################################################################################################################################################################
#HOME PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Home page view function
def index(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "Management/index.html",context)

#################################################################################################################################################################################
#LIST OF ITEMS PAGE VIEW FUNCTION
#################################################################################################################################################################################

#List of Items page view function
def list_items(request):
    title = 'List of list_items'
    # Queryset to get Stock Objects from Database
    queryset = Stock.objects.all()
    context = {
	"title": title,
    "queryset": queryset,
	}
    return render(request, "Management/list_items.html",context)

#################################################################################################################################################################################
#ADD ITEMS PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Add Items page view function
def add_items(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
        
	context = {
		"form": form,
		"title": "Add Item",
	}
	return render(request, "Management/add_items.html", context)