# Generated by Django 4.0.2 on 2022-02-18 07:22

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='username', unique=True, verbose_name='User URL'),
        ),
    ]