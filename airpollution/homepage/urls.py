from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('LosAngeles/', views.los_angeles, name='Los Angeles'),
	path('NewYork/', views.newyork, name='New York'),
	path('SanDiego/', views.san_diego, name='San Diego'),
]