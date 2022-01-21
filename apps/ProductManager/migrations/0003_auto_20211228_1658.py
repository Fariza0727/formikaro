# Generated by Django 3.1.7 on 2021-12-28 14:58

from django.db import migrations, models
import django.db.models.deletion
import thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManager', '0002_videoformat'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the image e.g Video Preview ', max_length=255, unique=True)),
                ('display_order', models.PositiveSmallIntegerField(help_text='Order of display value e.g. 1, the lowest ranked image will be displayed first')),
                ('image', thumbnails.fields.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='ProductManager.product')),
            ],
            options={
                'db_table': 'fo_product_image',
            },
        ),
        migrations.RenameModel(
            old_name='ProductTextModel',
            new_name='ProductText',
        ),
        migrations.CreateModel(
            name='ProductImageText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc_short', models.TextField()),
                ('desc_long', models.TextField()),
                ('default', models.BooleanField(blank=True, default=False)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ProductManager.language')),
                ('product_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_texts', to='ProductManager.productimage')),
            ],
            options={
                'db_table': 'fo_product_image_text',
            },
        ),
    ]