# Generated by Django 4.0 on 2021-12-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0018_comment_alter_product_description_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Test Product - 53 ', max_length=100),
        ),
    ]