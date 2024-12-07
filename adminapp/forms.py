from django import forms
from .models import Recipe_suggestor

class TaskForm(forms.ModelForm):
    class Meta:
        model = Recipe_suggestor
        fields=['ingredients', 'recipe']

