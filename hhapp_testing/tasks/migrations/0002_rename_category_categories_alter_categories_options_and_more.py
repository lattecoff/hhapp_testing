# Generated by Django 5.0.4 on 2024-05-06 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categories',
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='refrigerators',
            options={'verbose_name': 'Refrigerator', 'verbose_name_plural': 'Refrigerators'},
        ),
    ]
