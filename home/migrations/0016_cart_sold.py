# Generated by Django 3.2.2 on 2021-05-25 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_cart_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]