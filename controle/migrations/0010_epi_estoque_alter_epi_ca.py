# Generated by Django 5.1.6 on 2025-02-10 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0009_alter_epi_ca_alter_epi_tamanho'),
    ]

    operations = [
        migrations.AddField(
            model_name='epi',
            name='estoque',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='epi',
            name='ca',
            field=models.CharField(max_length=20),
        ),
    ]
