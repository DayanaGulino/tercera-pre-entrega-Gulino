# Generated by Django 5.0.2 on 2024-03-12 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_rename_nombre_cursos_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=48)),
                ('comision', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cursos',
        ),
    ]
