# Generated by Django 3.2.5 on 2021-07-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_prdlist_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prdlist',
            name='stock',
            field=models.IntegerField(max_length=500),
        ),
    ]
