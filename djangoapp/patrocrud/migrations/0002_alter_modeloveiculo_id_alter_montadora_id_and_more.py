# Generated by Django 5.1.2 on 2024-10-13 23:28

import django_ulid.models
import ulid.api.api
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patrocrud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeloveiculo',
            name='id',
            field=django_ulid.models.ULIDField(default=ulid.api.api.Api.new, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='montadora',
            name='id',
            field=django_ulid.models.ULIDField(default=ulid.api.api.Api.new, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='id',
            field=django_ulid.models.ULIDField(default=ulid.api.api.Api.new, editable=False, primary_key=True, serialize=False),
        ),
    ]
