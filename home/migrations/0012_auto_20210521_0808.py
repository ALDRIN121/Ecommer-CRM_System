# Generated by Django 3.2.2 on 2021-05-21 02:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_transact_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('brand_pd', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Quantity', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='transact',
            name='Total_Price',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]