# Generated by Django 3.2.2 on 2021-05-21 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_cart_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Total_Price',
            field=models.IntegerField(max_length=500),
        ),
    ]
