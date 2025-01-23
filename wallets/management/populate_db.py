# filepath: /home/fernando/Documentos/desafio/wallets/management/commands/populate_db.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from wallets.models import Wallet, Transaction

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **kwargs):
        user1 = User.objects.create_user(username='user1', password='password')
        user2 = User.objects.create_user(username='user2', password='password')
        wallet1 = Wallet.objects.create(user=user1, balance=1000.00)
        wallet2 = Wallet.objects.create(user=user2, balance=500.00)
        Transaction.objects.create(sender=wallet1, receiver=wallet2, amount=100.00, description='Initial transaction')
        self.stdout.write(self.style.SUCCESS('Database populated with initial data'))