"""PosSystem URL Configuration"""

from django.contrib import admin
from django.urls import include, path

# Imports Views For Management to Render Content.
from Management import views

'''Here we have imported (include)-: this allows us to add the Management url pattern
as done below this is to avoid filling up all our urls in this page'''

''' End Of Import'''
#-------------------------------#

urlpatterns = [
    path('admin/', admin.site.urls),
    # Includes Management url patterns
    path('', include('Management.urls')),
]
