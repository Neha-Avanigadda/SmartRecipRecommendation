import path
from django.urls import path, include
from . import views

from . import views
from .views import chatbot_response

urlpatterns=[
    path('', views.projecthomepage, name='projecthomepage'),
    path('ProjectLoginHomePage/', views.ProjectLoginHomePage, name='ProjectLoginHomePage'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('logout/', views.logout, name='logout'),
    path('ingredientHomePage/', views.ingredientHomePage, name='ingredientHomePage'),
    path('recipe_detail/', views.recipe_detail, name='recipe_detail'),
    path('recipies/', views.recipies, name='recipies'),
    path('chatbot-response/', views.chatbot_response, name='chatbot_response'),
    path('shopping_list/', views.shopping_list, name='shopping_list'),
    path('place-order/<int:product_id>/', views.place_order, name='place_order'),
    path('favorite_list/', views.favorite_list, name='favorite_list'),
    path('history_list/', views.history_list, name='history_list'),
]