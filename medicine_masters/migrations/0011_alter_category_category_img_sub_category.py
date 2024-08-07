# Generated by Django 5.0 on 2023-12-16 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0010_remove_category_category_detail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('subcategory_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('subcategory_name', models.CharField(max_length=150, unique=True)),
                ('subcategory_img', models.ImageField(null=True, upload_to='images/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine_masters.category')),
            ],
        ),
    ]
