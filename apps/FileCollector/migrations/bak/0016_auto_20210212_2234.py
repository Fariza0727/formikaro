# Generated by Django 3.1.6 on 2021-02-12 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileCollector', '0015_order_placed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='placed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]