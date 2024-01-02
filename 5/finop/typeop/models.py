from django.db import models


# Create your models here.

class Sale(models.Model):
    amount = models.FloatField(max_length=50)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.amount, self.date


class Purchase(models.Model):
    amount = models.FloatField(max_length=50)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.amount, self.date


class Transaction(models.Model):
    transaction_types = (
        ('Purchase', 'Purchase'),
        ('Sale', 'Sale')
    )
    amount = models.FloatField(max_length=50)
    type_transaction = models.CharField(max_length=50, blank=True, null=True, choices=transaction_types)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.amount, self.date, self.type_transaction
