# Generated by Django 5.0.1 on 2024-02-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0075_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
