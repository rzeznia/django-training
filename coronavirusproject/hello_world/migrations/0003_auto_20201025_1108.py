# Generated by Django 3.1.2 on 2020-10-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0002_auto_20201025_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[(1, 'male'), (2, 'female'), (3, 'other')], max_length=1),
        ),
    ]