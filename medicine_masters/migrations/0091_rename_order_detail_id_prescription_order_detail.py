# Generated by Django 5.0.1 on 2024-02-17 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0090_remove_prescription_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='order_detail_id',
            new_name='order_detail',
        ),
    ]