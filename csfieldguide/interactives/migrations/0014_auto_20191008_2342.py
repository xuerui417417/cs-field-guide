# Generated by Django 2.2.3 on 2019-10-08 23:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactives', '0013_interactive_is_interactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactive',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
    ]
