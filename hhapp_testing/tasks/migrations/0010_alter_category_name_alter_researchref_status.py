# Generated by Django 5.0.4 on 2024-05-09 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='researchref',
            name='status',
            field=models.CharField(choices=[('success', 'Success'), ('fail', 'Fail'), ('in_process', 'In Process')], max_length=50),
        ),
    ]
