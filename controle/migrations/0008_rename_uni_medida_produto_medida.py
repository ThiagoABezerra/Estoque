# Generated by Django 5.1.6 on 2025-02-08 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0007_departamento_alter_usuario_departamento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='uni_medida',
            new_name='medida',
        ),
    ]
