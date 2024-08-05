# Generated by Django 5.0.7 on 2024-07-14 14:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_notemodel_uuid_field_alter_notemodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notemodel',
            name='uuid_field',
            field=models.UUIDField(default=uuid.UUID('9073926b-929f-31c2-abc9-fad77ae3e8eb'), editable=False, unique=True),
        ),
    ]
