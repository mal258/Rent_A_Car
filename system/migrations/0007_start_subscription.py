# Generated by Django 3.0.5 on 2020-04-20 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_auto_20200420_0400'),
    ]

    operations = [
        migrations.CreateModel(
            name='start_subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('payment_type', models.CharField(max_length=10)),
                ('credit_card_number', models.IntegerField(max_length=30)),
                ('credit_card_name', models.CharField(max_length=30)),
                ('expiry_date', models.DateField()),
                ('cvv', models.IntegerField()),
            ],
        ),
    ]