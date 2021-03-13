from django import forms
from .models import Stock

# Forms Used to Create Stocks
class StockCreateForm (forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'item_name', 'quantity']

class StockSearchForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['item_name']

# Form Used to Issue Out Items
class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['issue_quantity', 'issue_to']

# Form Used to Recieve and Add Items to Stock
class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['receive_quantity']

# Form Used to Create Reorder Level
class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['reorder_level']