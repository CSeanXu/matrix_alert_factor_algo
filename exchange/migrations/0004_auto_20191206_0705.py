# Generated by Django 3.0 on 2019-12-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0003_auto_20191206_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='symbol_type',
            field=models.CharField(choices=[('LOWERCASE', 'LOWERCASE'), ('UPPERCASE', 'UPPERCASE'), ('LOWER_HYPHEN', 'LOWER_HYPHEN'), ('UPPER_HYPHEN', 'UPPER_HYPHEN'), ('LOWER_UNDERSCORE', 'LOWER_UNDERSCORE'), ('UPPER_UNDERSCORE', 'UPPER_UNDERSCORE')], default='UPPER_UNDERSCORE', max_length=128),
        ),
    ]