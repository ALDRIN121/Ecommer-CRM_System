# Generated by Django 2.2.16 on 2021-04-14 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_review_review_analysis'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='enquired',
            field=models.BooleanField(default=False),
        ),
    ]