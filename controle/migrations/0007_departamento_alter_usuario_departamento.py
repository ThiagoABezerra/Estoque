# Generated by Django 5.1.6 on 2025-02-08 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0006_produto_peso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='controle_departamento', to='controle.departamento'),
        ),
    ]
