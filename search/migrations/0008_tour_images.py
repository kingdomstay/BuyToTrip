# Generated by Django 4.0.1 on 2022-07-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_tour_price_alter_tour_arrival_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='images',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
