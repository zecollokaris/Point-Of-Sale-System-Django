from django.shortcuts import render, redirect

from .models import *

from .forms import *

from django.contrib import messages

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
        messages.success(request, 'Successfully Saved')
        return redirect('/list_items')
    context = {
		"form": form,
		"title": "Add Item",
	}
    return render(request, "Management/add_items.html", context)


#################################################################################################################################################################################
#STOCK DETAIL PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Stock Detail page view function
def stock_detail(request, pk):
	queryset = Stock.objects.get(id=pk)
	context = {
		"queryset": queryset,
	}
	return render(request, "Management/stock_detail.html", context)


#################################################################################################################################################################################
#ISSUE ITEM PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Issue Item page view function
def issue_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
        # Subtracts (Issue Quantity) from (Quantity)
		instance.quantity -= instance.issue_quantity
        # Display Notification
		messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
		instance.save()

		return redirect('/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": 'Issue ' + str(queryset.item_name),
		"queryset": queryset,
		"form": form,
		"username": 'Issue By: ' + str(request.user),
	}
	return render(request, "Management/add_items.html", context)


#################################################################################################################################################################################
#RECEIVE ITEM PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Receive Item page view function
def receive_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
        # Adds (Received Quantity) to (Quantity)
		instance.quantity += instance.receive_quantity
		instance.save()
		messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")

		return redirect('/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())
	context = {
			"title": 'Reaceive ' + str(queryset.item_name),
			"instance": queryset,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
	return render(request, "Management/add_items.html", context)

#################################################################################################################################################################################