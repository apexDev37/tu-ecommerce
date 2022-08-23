from django.urls import path

from . import views


API_VERSION = 'api/v1/'

urlpatterns = [
    path('products/', views.get_all_products, name='products'),
]
