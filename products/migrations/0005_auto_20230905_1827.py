# Generated by Django 3.2.20 on 2023-09-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_image_1_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-is_sold']},
        ),
        migrations.AddField(
            model_name='product',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]