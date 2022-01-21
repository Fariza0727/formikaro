# Generated by Django 3.1.5 on 2021-05-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormikoBot', '0007_asset_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='tasks',
            field=models.ManyToManyField(blank=True, related_name='assets', to='FormikoBot.Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('OP', 'OPEN'), ('AC', 'ACTIVE'), ('FD', 'FAILED'), ('CM', 'COMPLETE')], default='OP', max_length=8),
        ),
    ]