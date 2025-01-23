# filepath: /home/fernando/Documentos/desafio/wallets/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer, UserSerializer
from django.contrib.auth.models import User

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class WalletDetailView(generics.RetrieveAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class AddBalanceView(APIView):
    def post(self, request, pk):
        wallet = Wallet.objects.get(pk=pk)
        amount = request.data.get('amount')
        wallet.balance += float(amount)
        wallet.save()
        return Response({'status': 'balance added'})

class CreateTransactionView(APIView):
    def post(self, request):
        sender = Wallet.objects.get(user=request.user)
        receiver = Wallet.objects.get(user__username=request.data.get('receiver'))
        amount = float(request.data.get('amount'))
        description = request.data.get('description', '')
        if sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
            sender.save()
            receiver.save()
            Transaction.objects.create(sender=sender, receiver=receiver, amount=amount, description=description)
            return Response({'status': 'transaction successful'})
        return Response({'status': 'insufficient balance'}, status=400)

class ListTransactionsView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(sender__user=user)

class TransactionHistoryView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        queryset = Transaction.objects.filter(sender__user=user)
        if start_date and end_date:
            queryset = queryset.filter(timestamp__range=[start_date, end_date])
        return queryset