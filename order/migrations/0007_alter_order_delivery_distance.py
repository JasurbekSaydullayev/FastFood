# Generated by Django 5.0.4 on 2024-04-25 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_delivery_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_distance',
            field=models.FloatField(default=0),
        ),
    ]
