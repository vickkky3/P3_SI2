# Generated by Django 4.2.13 on 2025-04-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votoApp', '0002_alter_voto_idcircunscripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='voto',
            name='instancia',
            field=models.CharField(default=1, max_length=24),
        ),
    ]
