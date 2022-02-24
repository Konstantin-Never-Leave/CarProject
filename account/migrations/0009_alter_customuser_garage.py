# Generated by Django 4.0.2 on 2022-02-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0011_alter_usercar_slug_alter_usercar_vin'),
        ('account', '0008_alter_customuser_serviced_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='garage',
            field=models.ManyToManyField(blank=True, related_name='profile_owner', to='car.UserCar', verbose_name='Profile owner'),
        ),
    ]