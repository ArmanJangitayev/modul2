# Generated by Django 5.0 on 2024-01-01 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typeop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='Amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='Amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='Amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='Description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='Type_transaction',
        ),
        migrations.AddField(
            model_name='transaction',
            name='type_transaction',
            field=models.CharField(blank=True, choices=[('Purchase', 'Purchase'), ('Sale', 'Sale')], max_length=50, null=True),
        ),
    ]