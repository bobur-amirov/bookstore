# Generated by Django 4.0.3 on 2022-04-14 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
