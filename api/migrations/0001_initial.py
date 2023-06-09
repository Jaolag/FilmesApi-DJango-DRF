# Generated by Django 3.0.14 on 2023-05-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=8)),
                ('genero', models.CharField(choices=[('DRAMA', 'DRAMA'), ('COMEDIA', 'COMÉDIA')], max_length=8)),
                ('ano', models.PositiveIntegerField()),
                ('duracao', models.PositiveIntegerField()),
            ],
        ),
    ]
