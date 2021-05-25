# Generated by Django 3.2.3 on 2021-05-25 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]