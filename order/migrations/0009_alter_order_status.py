# Generated by Django 5.0.4 on 2024-04-30 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_remove_order_delivered_remove_order_order_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Qabul qilindi', max_length=50),
        ),
    ]
