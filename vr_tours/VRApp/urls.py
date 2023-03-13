from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),   
	path('sign_up/', views.SignUpView.as_view(), name='signup'),
	path('shop/', views.shop, name="shop"),
	path('countries/<str:title>/', views.countries, name='countries'),
	path('cities/<str:title>/', views.cities, name='cities'),
	path('historical_sites/', views.historicalSites, name="historical_sites"),
	path('animal_parks/', views.animalParks, name="animal_parks"),
	path('recreation_centers/', views.recreationCenters, name="recreation_centers"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]

