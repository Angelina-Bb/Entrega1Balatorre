# Generated by Django 4.1.3 on 2022-11-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appentrega', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.BooleanField(),
        ),
    ]