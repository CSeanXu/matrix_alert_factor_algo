# Generated by Django 2.2.8 on 2019-12-19 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
        ('trade', '0003_auto_20191219_0545'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='trade',
            unique_together={('exchange', 'symbol', 'amount', 'price', 'trade_time')},
        ),
    ]
