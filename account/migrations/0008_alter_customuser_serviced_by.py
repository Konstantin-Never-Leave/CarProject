# Generated by Django 4.0.2 on 2022-02-22 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_commercialuser_legal_name_commercialuser_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='serviced_by',
            field=models.ManyToManyField(blank=True, default=None, related_name='serviced_by', to='account.CommercialUser', verbose_name='Service used'),
        ),
    ]
