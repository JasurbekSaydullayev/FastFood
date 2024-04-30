# Generated by Django 5.0.4 on 2024-04-30 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_distance',
        ),
        migrations.AddField(
            model_name='order',
            name='location_lang',
            field=models.CharField(default='41.3422602', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='location_long',
            field=models.CharField(default='69.3371096', max_length=50),
        ),
    ]
