# Generated by Django 4.2.5 on 2023-10-04 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('tiempo', models.CharField(blank=True, max_length=10, null=True)),
                ('dificultad', models.CharField(blank=True, max_length=10, null=True)),
                ('porciones', models.IntegerField()),
                ('ingredientes', models.TextField()),
                ('pasos', models.TextField()),
                ('img', models.CharField(max_length=100)),
            ],
        ),
    ]
