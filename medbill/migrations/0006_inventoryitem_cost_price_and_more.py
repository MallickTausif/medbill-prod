# Generated by Django 4.2.7 on 2024-01-15 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medbill', '0005_remove_billing_medicines_alter_billingitem_medicine_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='cost_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2024, 7, 13)),
        ),
    ]
