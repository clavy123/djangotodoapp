from django import forms
from .models import Todoapp
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todoapp
        fields="__all__"