# Generated by Django 4.2.6 on 2023-10-22 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0003_remove_recetas_img_alter_recetas_dificultad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='categoria',
            field=models.CharField(choices=[('Entradas', 'Entradas'), ('Platos Principales', 'Platos Principales'), ('Postres', 'Postres'), ('Bebidas', 'Bebidas'), ('Cocina Internacional', 'Cocina Internacional'), ('Comida Saludable', 'Comida Saludable'), ('Ocasiones Especiales', 'Ocasiones Especiales')], default='Entradas', max_length=30),
        ),
    ]
