# Generated by Django 5.0.7 on 2024-07-14 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_notemodel_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notemodel',
            options={'ordering': ['username']},
        ),
    ]
