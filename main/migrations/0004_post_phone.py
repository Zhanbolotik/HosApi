# Generated by Django 3.1 on 2021-01-28 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210128_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.CharField(default='+996700000000', max_length=15),
        ),
    ]
