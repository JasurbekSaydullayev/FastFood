# Generated by Django 5.0.4 on 2024-04-23 10:22

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivered', models.BooleanField(default=False)),
                ('order_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.food')),
            ],
        ),
    ]
