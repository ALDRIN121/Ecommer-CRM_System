# Generated by Django 3.2.5 on 2021-07-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_prdlist_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prdlist',
            name='stock',
            field=models.CharField(max_length=500),
        ),
    ]