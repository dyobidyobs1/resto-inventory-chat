# Generated by Django 3.2.11 on 2023-04-18 21:58

from django.db import migrations, models
import inventoryapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0002_alter_orderprocess_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderprocess',
            name='reference_number',
            field=models.CharField(blank=True, default=inventoryapp.models.create_rand_id, editable=False, max_length=20, null=True),
        ),
    ]