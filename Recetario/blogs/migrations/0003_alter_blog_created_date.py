# Generated by Django 4.2.6 on 2023-10-22 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateField(auto_created=True, auto_now_add=True),
        ),
    ]
