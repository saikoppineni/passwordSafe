# Generated by Django 5.0.7 on 2024-07-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_notemodel_options_notemodel_mainpass_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notemodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='notemodel',
            name='mainuser',
            field=models.CharField(default=True, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
