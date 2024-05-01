# Generated by Django 4.2.7 on 2023-12-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_remove_transaction_bankrupt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer_money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.IntegerField(blank=True, choices=[(1, 'Deposite'), (2, 'Withdrawal'), (3, 'Loan'), (4, 'Loan Paid'), (5, 'transfer')], null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
