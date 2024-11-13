from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, decorators
from .forms import registerForm, IncomeForm, ExpenseForm, loginForm
from .models import Income, Expense
from django.db.models import Sum
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

@decorators.login_required(login_url='login')
def home_view(request):
    income = Income.objects.filter(user=request.user)
    total_income = income.aggregate(Sum('amount'))['amount__sum']
    
    expense_obj = Expense.objects.filter(user=request.user).order_by('-date')[:4]
    total_expenses = expense_obj.aggregate(Sum('amount'))['amount__sum']
    
    return render(request, 'home.html', context={'expense_obj':expense_obj, 'income':income, 'total_income':total_income, 'total_expenses':total_expenses})



#
def login_view(request):
    form = loginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user_obj = authenticate(request, username=username, password=password)
        login(request, user_obj)
        return redirect('home')  # Redirect to your desired page after login
    return render(request, 'login.html', {'form': form})


def register_view(request):
    form = registerForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(request, 'register.html', context={"form":form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')
    




@decorators.login_required(login_url='login')
def expenses_view(request):     
    expense_obj = Expense.objects.filter(user=request.user).order_by('-date')
    total_expenses = expense_obj.aggregate(Sum('amount'))['amount__sum']
        
    return render(request, 'expenses.html', context={'expense_obj':expense_obj, 'total_expenses':total_expenses})



@decorators.login_required(login_url='login')
def expense_add_view(request):
    form = ExpenseForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        amount = form.cleaned_data.get('amount')
        description = form.cleaned_data.get('description')
        category = form.cleaned_data.get('category')
        Expense.objects.create(user=request.user, amount=amount, description=description, category=category).save()
        return redirect('home')
    return render(request, 'expense_add.html', context={'form':form})



@decorators.login_required(login_url='login')
def expense_update_view(request, id):
    expense = get_object_or_404(Expense, user=request.user, id=id)
    form = ExpenseForm(instance=expense)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'expense_update.html', context={'form':form, 'id':id})



@decorators.login_required(login_url='login')
def expense_delete_view(request, id):
    expense_id = get_object_or_404(Expense, user=request.user, id=id)
    expense_id.delete()
    return redirect('home')
    



@decorators.login_required(login_url='login')
def income_add_view(request):
    form = IncomeForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        amount = form.cleaned_data.get('amount')
        source = form.cleaned_data.get('source')
        user = request.user
        Income.objects.create(user=user, amount=amount, source=source).save()
        return redirect('home')
    return render(request, 'income_add.html', context={'form':form})



@decorators.login_required(login_url='login')
def income_update_view(request, id):
    income = get_object_or_404(Income, user=request.user, id=id)
    form = IncomeForm(instance=income)
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'income_update.html', context={'id':id, 'form':form})




@decorators.login_required(login_url='login')
def income_delete_view(request, id):
    income = get_object_or_404(Income, user=request.user, id=id)
    income.delete()
    return redirect('home')
