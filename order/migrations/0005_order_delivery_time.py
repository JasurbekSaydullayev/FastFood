# Generated by Django 5.0.4 on 2024-04-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_delivery_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.IntegerField(default=0),
        ),
    ]
