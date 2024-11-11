"""
URL configuration for budgetTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name='register'),

    # 
    path('expense-add/', views.expense_add_view, name='expense-add'),
    path('expense-update/<int:id>', views.expense_update_view, name="expense-update"),
    path('expense-delete/<int:id>', views.expense_delete_view, name='expense-delete'),

    #
    path('income-add/', views.income_add_view, name='income-add'),
    path('income-update/<int:id>', views.income_update_view, name='income-update'),
    path('income-delete/<int:id>', views.income_delete_view, name='income-delete'),
]
