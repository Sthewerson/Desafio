# filepath: /home/fernando/Documentos/desafio/wallets/models.py
from django.contrib.auth.models import User
from django.db import models

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s wallet"

class Transaction(models.Model):
    sender = models.ForeignKey(Wallet, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Wallet, related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Transaction from {self.sender.user.username} to {self.receiver.user.username} for {self.amount}"