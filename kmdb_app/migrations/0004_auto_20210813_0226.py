# Generated by Django 3.2.6 on 2021-08-13 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kmdb_app', '0003_alter_movie_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='movie',
        ),
        migrations.AddField(
            model_name='genre',
            name='movie',
            field=models.ManyToManyField(to='kmdb_app.Movie'),
        ),
    ]
