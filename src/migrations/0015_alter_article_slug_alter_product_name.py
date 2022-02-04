# Generated by Django 4.0 on 2021-12-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0014_merge_20211217_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Test Product - 16 ', max_length=100),
        ),
    ]
