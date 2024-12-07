from django.shortcuts import render, get_object_or_404
from .models import Recipe


def recipe_detail(request):
    recipe_name = request.GET.get('recipe_name', None)
    recipe = None
    if recipe_name:
        recipe = get_object_or_404(Recipe, name__iexact=recipe_name)

    return render(request, 'recipe/recipe_detail.html',)



