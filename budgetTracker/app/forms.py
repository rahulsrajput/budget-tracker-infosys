from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Income, Expense
from django import forms

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount','source']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'description', 'category']

