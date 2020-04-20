# Generated by Django 3.0.5 on 2020-04-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_auto_20200420_0513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='content',
        ),
        migrations.AddField(
            model_name='car',
            name='rent_loc',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='vehicle_cond',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='loc_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.CharField(choices=[('small car', 'SMALL CAR'), ('full-size_car', 'FULL-SIZE CAR'), ('truck', 'TRUCK'), ('luxury', 'LUXURY')], max_length=50),
        ),
    ]