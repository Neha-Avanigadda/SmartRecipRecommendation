from django.urls import path, include
from . import views
app_name='ingredientManagement'
urlpatterns = [
    path('ingredientHomePage/', views.ingredientHomePage, name='ingredientHomePage')
]