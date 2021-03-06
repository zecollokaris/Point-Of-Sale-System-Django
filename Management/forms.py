from django import forms
from .models import Stock

#Forms Used to Create Stocks
class StockCreateForm (forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'item_name', 'quantity']
