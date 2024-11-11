from django.contrib import admin
from .models import Income , Expense, Budget

# Register your models here.
@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    model = Income
    list_display = ('id','user','amount','date')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    model = Expense
    list_display = ('id', 'user', 'category', 'amount' ,'date')


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    model = Budget
    list_display = ('id', 'user', 'category', 'amount')