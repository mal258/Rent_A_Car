# Generated by Django 3.0.5 on 2020-05-01 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_startsubscribe_acc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_account', models.IntegerField()),
                ('company_account', models.IntegerField()),
            ],
        ),
    ]
