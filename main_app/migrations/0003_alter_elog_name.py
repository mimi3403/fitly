# Generated by Django 3.2.4 on 2021-07-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_elog_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elog',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
