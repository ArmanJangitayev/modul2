from django import forms
from .models import Sale, Purchase, Transaction


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
