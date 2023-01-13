# Generated by Django 4.1.4 on 2023-01-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0006_recharge'),
    ]

    operations = [
        migrations.AddField(
            model_name='recharge',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('accept', 'accept'), ('rejected', 'rejected')], default='pending', max_length=50),
        ),
    ]
