# Generated by Django 2.2.12 on 2021-04-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210409_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='transact',
            name='review_given',
            field=models.BooleanField(default=False),
        ),
    ]