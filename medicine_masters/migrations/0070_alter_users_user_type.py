# Generated by Django 5.0.1 on 2024-01-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0069_alter_users_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=2),
        ),
    ]
