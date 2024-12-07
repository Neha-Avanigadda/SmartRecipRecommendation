from django.contrib.auth.models import User, auth
from django.http import JsonResponse

from adminapp.models import Recipe_suggestor


def projecthomepage(request):
    return render(request,'adminapp/ProjectHomePage.html')

def ProjectLoginHomePage(request):
    return render(request, 'adminapp/ProjectLoginHomePage.html')
def UserRegisterPageCall(request):
    return render(request, 'adminapp/UserRegisterPage.html')

def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/UserRegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/UserRegisterPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/UserRegisterPage.html')
    else:
        return render(request, 'adminapp/UserRegister.html')

def UserLoginPageCall(request):
    return render(request, 'adminapp/UserLoginPage.html')
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404


def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        return redirect('ProjectLoginHomePage')
    else:
        return render(request, 'adminapp/UserLoginPage.html')

def logout(request):
    auth.logout(request)
    return render(request, 'adminapp/ProjectHomePage.html')

def ingredientHomePage(request):
    return render(request, 'ingredientManagement/ingredientHomePage.html')


def recipe_detail(request):
    recipe_name = request.GET.get('recipe_name.html', None)
    recipe = None
    if recipe_name:
        recipe = get_object_or_404(recipe, name__iexact=recipe_name)

    return render(request, 'recipe/recipe_detail.html',)


def recipies(request):
    r = Recipe_suggestor.objects.all()
    return render(request, 'adminapp/student_list.html', {'recipes': r})


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai  # Install via `pip install openai`

# Set up your OpenAI API key

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            user_message = data.get('message', '')

            if not user_message:
                return JsonResponse({'response': 'Please provide a message.'})

            # Send the message to OpenAI GPT model
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Use gpt-4 or other models like gpt-3.5-turbo
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message},
                ]
            )

            # Extract AI's response
            bot_message = response['choices'][0]['message']['content'].strip()

            return JsonResponse({'response': bot_message})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

from django.shortcuts import render, redirect
from .models import Product, Order
from django.contrib.auth.decorators import login_required

# View to display shopping list page
def shopping_list(request):
    products = Product.objects.all()
    return render(request, 'adminapp/shopping_list.html', {'products': products})

# View to handle order placement
@login_required
def place_order(request, product_id):
    product = Product.objects.get(id=product_id)
    order = Order.objects.create(user=request.user, product=product)
    return redirect('order_confirmation', order_id=order.id)



def favorite_list(request):
    products = Product.objects.all()
    return render(request, 'adminapp/favorite_list.html', {'products': products})
def history_list(request):
    products = Product.objects.all()
    return render(request, 'adminapp/history_list.html', {'products': products})