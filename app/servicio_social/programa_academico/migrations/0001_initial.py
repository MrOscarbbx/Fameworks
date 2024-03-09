# Generated by Django 5.0.2 on 2024-02-13 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramaAcademico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('unidad_academica', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='programa_academico.unidadacademica', verbose_name='Unidad Academica')),
            ],
        ),
    ]
