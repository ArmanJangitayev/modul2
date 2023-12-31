# Generated by Django 5.0 on 2024-01-01 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.FloatField(max_length=50)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.FloatField(max_length=50)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.FloatField(max_length=50)),
                ('Type_transaction', models.CharField(blank=True, max_length=50, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
