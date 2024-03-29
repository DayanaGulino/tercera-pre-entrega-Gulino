# Generated by Django 5.0.2 on 2024-03-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='agencias',
            fields=[
                ('nombre', models.CharField(max_length=48)),
                ('tipo', models.CharField(max_length=48)),
                ('id', models.CharField(max_length=48, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Agencia',
                'verbose_name_plural': 'Agencias',
            },
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=48)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_agencia', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='staff',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Staff', 'verbose_name_plural': 'Staff'},
        ),
    ]
