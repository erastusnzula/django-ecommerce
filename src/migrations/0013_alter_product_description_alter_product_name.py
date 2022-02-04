# Generated by Django 4.0 on 2021-12-17 12:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0012_alter_product_description_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(default='I love this product so much.'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Test Product - 97 ', max_length=100),
        ),
    ]
