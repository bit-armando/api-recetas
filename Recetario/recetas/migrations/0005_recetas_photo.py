# Generated by Django 4.2.6 on 2023-10-22 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0004_alter_recetas_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='recetas',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='Recetas'),
        ),
    ]