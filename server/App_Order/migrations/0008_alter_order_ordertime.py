# Generated by Django 4.2.5 on 2023-09-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Order', '0007_alter_order_ordertime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordertime',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
