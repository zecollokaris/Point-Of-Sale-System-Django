from django.contrib import admin
from .forms import StockCreateForm

# Register your models here.
from .models import Stock 

class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['category', 'item_name', 'quantity']
   form = StockCreateForm
#    Enables Filter Database By Category In Admin Section
   list_filter = ['category']
#    Enables Search Database By Category & Name In Admin Section
   search_fields = ['category', 'item_name']

admin.site.register(Stock, StockCreateAdmin)
