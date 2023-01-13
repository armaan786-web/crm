# Generated by Django 4.1.4 on 2023-01-09 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm_app', '0007_recharge_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='kyc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=50)),
                ('branck', models.CharField(max_length=50)),
                ('ifsc_code', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
