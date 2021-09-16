from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import path, reverse_lazy
from .models import Expense
from .views import ExpenseListView


urlpatterns = [
    path('expense/list/',
         ExpenseListView.as_view(),
         name='expense-list'),
    path('expense/create/',
         CreateView.as_view(
            model=Expense,
            fields='__all__',
            success_url=reverse_lazy('expenses:expense-list')
         ),
         name='expense-create'),
    path('expense/<int:pk>/edit/',
         UpdateView.as_view(
            model=Expense,
            fields='__all__',
            success_url=reverse_lazy('expenses:expense-list')
         ),
         name='expense-edit'),
    path('expense/<int:pk>/delete/',
         DeleteView.as_view(
             model=Expense,
             success_url=reverse_lazy('expenses:expense-list')
         ),
         name='expense-delete'),
]
