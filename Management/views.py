from django.shortcuts import render, redirect

from .models import *

from .forms import StockCreateForm, StockSearchForm


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
    ListHeader = 'List of Items'
    form = StockSearchForm(request.POST or None)
    # Queryset to get Stock Objects from Database
    queryset = Stock.objects.all()
    context = {
        "ListHeader": ListHeader,
        "queryset": queryset,
        "form": form,
	}
    # Executes Search Once All Conditions Are Met
    if request.method == 'POST':
        queryset = Stock.objects.filter(item_name__icontains=form['item_name'].value()
        )
        context = {
        "form": form,
        "ListHeader": ListHeader,
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
        return redirect('/list_items')
    context = {
		"form": form,
		"title": "Add Item",
	}
    return render(request, "Management/add_items.html", context)