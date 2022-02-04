# Generated by Django 4.0 on 2021-12-13 09:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(default='Wow! I have never seen anything like this before.'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Test Product - 84 ', max_length=100),
        ),
    ]
