# filepath: /home/fernando/Documentos/desafio/wallets/urls.py
from django.urls import path
from .views import CreateUserView, UserDetailView, WalletDetailView, AddBalanceView, CreateTransactionView, ListTransactionsView, TransactionHistoryView

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='create_user'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('wallets/<int:pk>/', WalletDetailView.as_view(), name='wallet_detail'),
    path('wallets/<int:pk>/add_balance/', AddBalanceView.as_view(), name='add_balance'),
    path('transactions/', CreateTransactionView.as_view(), name='create_transaction'),
    path('transactions/list/', ListTransactionsView.as_view(), name='list_transactions'),
    path('transactions/history/', TransactionHistoryView.as_view(), name='transaction_history'),
]