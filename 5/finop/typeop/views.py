from django.shortcuts import render, get_object_or_404, redirect
from .models import Sale, Transaction, Purchase
from .forms import SaleForm, TransactionForm, PurchaseForm


def SaleList(request):
    sales = Transaction.objects.filter(type_transaction='Sale')
    purchases = Transaction.objects.filter(type_transaction='Purchase')

    return render(request, 'list_all.html',
                  {'sales': sales, 'purchases': purchases, 'transactions': Transaction.objects.all()}, )


def TransactionList(request):
    transactions = Transaction.objects.all()
    return render(request, 'list_all.html', {'transactions': transactions})


def PurchaseList(request):
    purchase = Purchase.objects.all()
    return render(request, 'list_all.html', {'purchase': purchase})


def PurchaseDetail(request, pk):
    purchase = get_object_or_404(Transaction, pk=pk)
    return render(request, 'purchase_detail.html', {'purchase': purchase})


def SaleDetail(request, pk):
    sale = get_object_or_404(Transaction, pk=pk)
    return render(request, 'sale_detail.html', {'sale': sale})


def TransactionDetail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(request, 'transaction_detail.html', {'transaction': transaction})


def PurchaseDelete(request, pk):
    purchase = get_object_or_404(Transaction, pk=pk)
    purchase.delete()
    return redirect('sale_list')


def SaleDelete(request, pk):
    sale = get_object_or_404(Transaction, pk=pk)
    sale.delete()
    return redirect('sale_list')


def TransactionDelete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect('sale_list')


def PurchaseCreate(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = PurchaseForm()
    return render(request, 'create_purchase.html', {'form': form})


def SaleCreate(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = SaleForm()
    return render(request, 'create_sale.html', {'form': form})


def TransactionCreate(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = TransactionForm()
    return render(request, 'create_transaction.html', {'form': form})
