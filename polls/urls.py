from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.search_form, name='search_form'),
	 path('', views.search, name='search'),
   
]
