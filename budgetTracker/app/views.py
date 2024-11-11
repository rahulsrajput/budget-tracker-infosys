from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import registerForm, IncomeForm, ExpenseForm
from .models import Income, Expense
from django.db.models import Sum

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        income = Income.objects.filter(user=request.user)
        total_income = income.aggregate(Sum('amount'))['amount__sum']
        
        expense_obj = Expense.objects.filter(user=request.user).order_by('-date')
        total_expenses = expense_obj.aggregate(Sum('amount'))['amount__sum']
        
        grouped_expense = {}
        for expense in expense_obj:
            if expense.date not in grouped_expense:
                grouped_expense[expense.date] = []
            grouped_expense[expense.date].append(expense)
        # print(grouped_expense)
        return render(request, 'home.html', context={'grouped_expense':grouped_expense, 'income':income, 'total_income':total_income, 'total_expenses':total_expenses})
    else:
        return redirect('login')



#
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
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
    




#
def expense_add_view(request):
    if request.user.is_authenticated:
        form = ExpenseForm(data=request.POST or None)
        if request.method == "POST" and form.is_valid():
            amount = form.cleaned_data.get('amount')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            Expense.objects.create(user=request.user, amount=amount, description=description, category=category).save()
            return redirect('home')
        return render(request, 'expense_add.html', context={'form':form})
    else:
        return redirect('login')
    

def expense_update_view(request, id):
    if request.user.is_authenticated:
        expense = get_object_or_404(Expense, user=request.user, id=id)
        form = ExpenseForm(instance=expense)
        if request.method == "POST":
            form = ExpenseForm(request.POST, instance=expense)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'expense_update.html', context={'form':form, 'id':id})
    else:
        return redirect('login')


def expense_delete_view(request, id):
    if request.user.is_authenticated:
        expense_id = get_object_or_404(Expense, user=request.user, id=id)
        expense_id.delete()
        return redirect('home')
    else:
        return redirect('login')



#
def income_add_view(request):
    if request.user.is_authenticated:
        form = IncomeForm(data=request.POST or None)
        if request.method == "POST" and form.is_valid():
            amount = form.cleaned_data.get('amount')
            source = form.cleaned_data.get('source')
            user = request.user
            Income.objects.create(user=user, amount=amount, source=source).save()
            return redirect('home')
        return render(request, 'income_add.html', context={'form':form})
    else:
        return redirect('login')
    

def income_update_view(request, id):
    if request.user.is_authenticated:
        income = get_object_or_404(Income, user=request.user, id=id)
        form = IncomeForm(instance=income)
        if request.method == "POST":
            form = IncomeForm(request.POST, instance=income)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'income_update.html', context={'id':id, 'form':form})
    else:
        return redirect('login')
    

def income_delete_view(request, id):
    if request.user.is_authenticated:
        income = get_object_or_404(Income, user=request.user, id=id)
        income.delete()
        return redirect('home')
    else:
        return redirect('login')