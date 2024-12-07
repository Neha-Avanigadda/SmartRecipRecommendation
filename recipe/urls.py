from django.urls import path
from . import views

urlpatterns = [
    path('recipe/', views.recipe_detail, name='recipe_detail'),
    path('shopping_list/', views.shopping_list, name='shopping_list'),
    path('place-order/<int:product_id>/', views.place_order, name='place_order'),
    path('favorite_list/', views.favorite_list, name='favorite_list'),
    path('history_list/', views.history_list, name='history_list'),
]
