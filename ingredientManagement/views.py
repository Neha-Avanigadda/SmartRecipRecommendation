from django.shortcuts import render
# Create your views here.
def ingredientHomePage(request):
    return render(request, 'ingredientManagement/ingredientHomePage.html')