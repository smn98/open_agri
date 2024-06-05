# Generated by Django 5.0.6 on 2024-06-05 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_alter_device_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='images/')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='devices.device')),
            ],
        ),
    ]
