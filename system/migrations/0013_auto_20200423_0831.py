# Generated by Django 3.0.5 on 2020-04-23 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0012_merge_20200421_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='rent_loc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vehicle', to='system.Location'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='system.UserDetails')),
            ],
        ),
    ]
