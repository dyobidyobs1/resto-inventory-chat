# Generated by Django 3.2.11 on 2023-05-07 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventoryapp', '0005_orderprocess_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderprocess',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
