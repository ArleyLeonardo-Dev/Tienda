# Generated by Django 5.1.1 on 2024-10-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0002_prodcutos_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodcutos',
            name='Tipo',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
