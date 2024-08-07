# Generated by Django 5.0.1 on 2024-02-19 11:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0097_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='prescription_img',
            field=models.ImageField(null=True, upload_to='media/prescription_img'),
        ),
        migrations.CreateModel(
            name='Prescription_Detail',
            fields=[
                ('prescription_detail_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('prescription_message', models.CharField(blank=True, max_length=150, null=True)),
                ('prescription_status', models.CharField(default='Pending For Approve', max_length=100)),
                ('order_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine_masters.order_detail')),
                ('prescription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine_masters.prescription')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
