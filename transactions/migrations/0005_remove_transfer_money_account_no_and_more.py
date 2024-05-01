# Generated by Django 4.2.7 on 2023-12-27 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userbankaccount_bankrupt'),
        ('transactions', '0004_transfer_money'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer_money',
            name='account_no',
        ),
        migrations.AddField(
            model_name='transfer_money',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions2', to='accounts.userbankaccount'),
        ),
        migrations.AddField(
            model_name='transfer_money',
            name='accountNO',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
