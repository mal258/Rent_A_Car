# Generated by Django 3.0.5 on 2020-04-20 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_auto_20200418_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mobileno', models.IntegerField(max_length=30)),
                ('birthdate', models.DateField()),
                ('address', models.CharField(max_length=30)),
                ('license_number', models.CharField(max_length=10)),
                ('license_place', models.CharField(max_length=30)),
            ],
        ),
    ]
