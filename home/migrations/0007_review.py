# Generated by Django 2.2.12 on 2021-04-09 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_transact_review_given'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=700)),
                ('brand_pd', models.CharField(max_length=100)),
            ],
        ),
    ]
