# Generated by Django 3.0 on 2019-12-06 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exchange', '0003_auto_20191206_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.Exchange')),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.Symbol')),
            ],
        ),
    ]