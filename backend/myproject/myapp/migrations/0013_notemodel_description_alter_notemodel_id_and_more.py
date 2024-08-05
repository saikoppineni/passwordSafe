# Generated by Django 5.0.7 on 2024-07-14 14:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_notemodel_description_alter_notemodel_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notemodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notemodel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='notemodel',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notemodel',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
