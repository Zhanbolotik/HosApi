# Generated by Django 3.1 on 2021-01-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210127_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(default='Bishkek', max_length=150),
        ),
        migrations.AddField(
            model_name='post',
            name='full_name',
            field=models.CharField(default='Anonimous', max_length=100),
        ),
    ]
