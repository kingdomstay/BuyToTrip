# Generated by Django 4.0.1 on 2022-07-06 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_hotel_tour_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='departure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='search.airport'),
        ),
    ]
