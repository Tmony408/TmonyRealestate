# Generated by Django 3.1.4 on 2021-03-22 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20210322_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='purchase_index',
            field=models.IntegerField(),
        ),
    ]