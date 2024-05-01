from django.contrib import admin
from .views import send_email_user
# from transactions.models import Transaction
from .models import Transaction
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_after_transaction', 'transaction_type', 'loan_approve']
    
    def save_model(self, request, obj, form, change):
        obj.account.balance += obj.amount
        obj.balance_after_transaction = obj.account.balance
        obj.account.save()

        send_email_user(obj.account.user, obj.amount, "Loan Approved", "transactions/loanApprove.html")
        super().save_model(request, obj, form, change)

