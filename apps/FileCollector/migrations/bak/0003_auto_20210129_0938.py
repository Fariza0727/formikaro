# Generated by Django 3.1.4 on 2021-01-29 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManager', '0001_initial'),
        ('FileCollector', '0002_auto_20210128_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ProductManager.language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ProductManager.language'),
            preserve_default=False,
        ),
    ]