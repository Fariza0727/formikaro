# Generated by Django 3.1.5 on 2021-09-07 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FileCollector', '0037_auto_20210907_1048'),
        ('FormikoAudit', '0006_auto_20210907_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='camerasetting',
            name='name',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shoot',
            name='settings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shoot_settings', to='FormikoAudit.camerasetting'),
        ),
        migrations.AlterField(
            model_name='shoot',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shoot_projects', to='FileCollector.project'),
        ),
    ]