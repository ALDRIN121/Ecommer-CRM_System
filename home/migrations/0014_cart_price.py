# Generated by Django 3.2.2 on 2021-05-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_cart_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
