from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Income, Expense
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-0 rounded'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'form-control bg-dark text-white border-0 rounded'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white border-0 rounded'}))
    password2 = forms.CharField(label='Password Confirmation',widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white border-0 rounded'}))



class loginForm(AuthenticationForm):
    # You can override the widget here directly for the form fields
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-0 rounded'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white border-0 rounded'}))




class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount','source']
        widgets = {
            'amount' : forms.NumberInput(attrs={'class':'form-control bg-dark text-white border-0 rounded'}),
            'source' : forms.TextInput(attrs={'class':'form-control bg-dark text-white border-0 rounded'})
        }



class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'description', 'category']
        widgets = {
            'amount' : forms.NumberInput(attrs={'class':'form-control bg-dark text-white border-0 rounded'}),
            'description' : forms.Textarea(attrs={'class':'form-control bg-dark text-white border-0 rounded'}),
            'category' : forms.Select(attrs={'class':'form-control bg-dark text-white border-0 rounded'}),
        }
